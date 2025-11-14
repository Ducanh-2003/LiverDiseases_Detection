from .model_loader import model
from PIL import Image
import io
import base64
import numpy as np

def get_prediction(img_bytes):
    if model is None:
        raise ValueError("Model unloaded.")
        
    img = Image.open(io.BytesIO(img_bytes))
    result = model(img)
    
    img_with_boxes = result[0].plot()
    img_result = Image.fromarray(img_with_boxes[..., :: -1])

    buf = io.BytesIO()
    img_result.save(buf, format = "JPEG")    
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    detections = []
    for box in result[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        detections.append({
            "class": model.names[class_id],
            "confidence": round(confidence, 2)
        })
        
    return {
        "image_base64": img_base64,
        "detections": detections
    }
                           
       