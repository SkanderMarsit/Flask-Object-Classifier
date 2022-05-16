import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image

imagenet_class_index = json.load(open('imagenet_class_index.json'))
model = models.densenet121(pretrained=True)
model.eval()

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_predictions(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)

    outputs = model.forward(tensor)
    _, indices = torch.sort(outputs, descending=True) 
    confidence = torch.nn.functional.softmax(outputs, dim=1)[0]

    idx_top1 = indices[0][0]
    top1 = imagenet_class_index[str(idx_top1.item())][1], confidence[idx_top1].item()
    
    return top1