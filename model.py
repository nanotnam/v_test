import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from unet import UNetPlusPlus

# Load model
def load_model():
    model_path = "model/model_epoch_40.pth"  # Đường dẫn tới file model
    device = torch.device('cpu')  # Chạy trên CPU

    # Khởi tạo mô hình
    model = UNetPlusPlus(in_channels=3, num_classes=1)  

    # Tải trọng số vào mô hình
    model.load_state_dict(torch.load(model_path, map_location=device))

    # Đặt chế độ evaluation
    model.eval()
    return model

# Run prediction
def predict(model, image_path):
    # Load image
    image = Image.open(image_path).convert("RGB")
    preprocess = transforms.Compose([
        transforms.Resize((1024, 1024)),
        transforms.ToTensor()
    ])
    input_tensor = preprocess(image).unsqueeze(0)

    # Inference
    with torch.inference_mode():
        output = model(input_tensor)
        mask = torch.sigmoid(output).squeeze().numpy()
        mask = (mask > 0.5).astype(np.uint8) * 255

    # Convert to PIL Image
    mask_image = Image.fromarray(mask)
    return mask_image
