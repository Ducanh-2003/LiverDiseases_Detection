from ultralytics import YOLO

def load_model(model_path = "best_model.pt"):
    try:
        model =YOLO(model_path)
        return model
    except Exception as e: 
        print(f"Error while loading model:{e}")
        return None
    
model = load_model()