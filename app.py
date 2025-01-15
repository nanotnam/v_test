from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from celery import Celery
import os
from celery_worker import run_inference


# Flask app
app = Flask(__name__)
CORS(app)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'
celery = Celery(app.name)
celery.conf.update(app.config)


# Endpoint nhận ảnh và cho vào model
@app.route('/inference', methods=['POST'])
def inference():
    if 'image' not in request.files:
        return jsonify({"error": "anh chua duoc upload"}), 400

    # Lưu ảnh vào static
    image = request.files['image']
    image_path = os.path.join("static", image.filename)
    image.save(image_path)

    # Bắt đầu cho ảnh vào model
    task = run_inference.delay(image_path)
    
    # tạo link kết quả
    link = f"http://127.0.0.1:5000/result/{task.id}" #thay port neu can

    return render_template('result.html', link=link)


# Endpoint nhận kết quả
@app.route('/result/<task_id>', methods=['GET'])
def result(task_id):
    task = run_inference.AsyncResult(task_id)

    if task.state == 'PENDING':
        # response = {
        #     "state": task.state,
        #     "status": "Chua xong, tai lai trang sau vai giay...  Processing, reload in a few seconds..."
        # }
        return render_template('phong_cho.html')

    elif task.state == 'SUCCESS':
        input_path, output_path = task.result
        return render_template('display_images.html', input_image=input_path, output_image=output_path)
    else:

        status = str(task.info)
        response = {
            "state": task.state,
            "status": status
        }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
