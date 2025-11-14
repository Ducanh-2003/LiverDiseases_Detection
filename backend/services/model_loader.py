from ultralytics import YOLO
import os

def load_model(model_path = None):
    try:
        if model_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            model_path = os.path.join(current_dir, '..', 'best_model.pt')
        model = YOLO(model_path)
        return model
    except Exception as e: 
        print(f"Error while loading model:{e}")
        return None
    
model = load_model()