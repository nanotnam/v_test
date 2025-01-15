from celery import Celery
from model import load_model, predict
import os

celery = Celery('celery_worker', broker='pyamqp://guest@localhost//', backend='rpc://')

model = load_model()

@celery.task(bind=True)
def run_inference(self, image_path):
    
    mask = predict(model, image_path)

    output_path = os.path.join("static", "output_" + os.path.basename(image_path))
    mask.save(output_path)

    return image_path, output_path


