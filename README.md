# viettel_test

# Cài đặt

Mở Docker (để tải Rabbitmq qua docker)

Vào terminal chạy
    virtualenv env

    source env/bin/activate

    pip install -r requirements.txt

    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management

# Sử dụng

Vào terminal chạy    
    celery -A celery_worker worker --loglevel=info

    lưu ý: dòng trên khởi động celery mặc định với 1 worker, để dùng nhiều worker hơn, cú pháp như sau:
    "celery -A celery_worker worker --loglevel=info -c 4"
    thay 4 bằng số worker. Check số core của CPU để xem số worker tối đa 

    python3 app.py

    Dùng Live Server Extension trên Visual Studio Code để mở /templates/index.html trên web browser
