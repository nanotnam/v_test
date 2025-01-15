from celery import Celery
from model import load_model, predict
import os

celery = Celery('celery_worker', broker='pyamqp://guest@localhost//', backend='rpc://')

# Load model once to avoid reloading for every task
model = load_model()


@celery.task(bind=True)
def run_inference(self, image_path):
    try:
        # Run inference
        mask = predict(model, image_path)

        # Save binary mask
        output_path = os.path.join("static", "output_" + os.path.basename(image_path))
        mask.save(output_path)

        return image_path, output_path
    except Exception as e:
        self.update_state(state='FAILURE', meta={'error': str(e)})
        raise

