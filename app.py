from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from celery import Celery
import os
from PIL import Image
import numpy as np
from io import BytesIO
from celery_worker import run_inference


# Flask app
app = Flask(__name__)
CORS(app)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Endpoint to receive image and start inference task
@app.route('/inference', methods=['POST'])
def inference():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    # Save image locally
    image = request.files['image']
    image_path = os.path.join("static", image.filename)
    image.save(image_path)

    # Start Celery task
    task = run_inference.delay(image_path)

    return jsonify({"task_id": task.id}), 202

# Endpoint to get inference result
@app.route('/result/<task_id>', methods=['GET'])
def result(task_id):
    task = run_inference.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            "state": task.state,
            "status": "Task is pending..."
        }
    elif task.state == 'SUCCESS':
        result_path = task.result
        return send_file(result_path, mimetype='image/png')
    else:
        response = {
            "state": task.state,
            "status": task.info.get('error', str(task.info))
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
