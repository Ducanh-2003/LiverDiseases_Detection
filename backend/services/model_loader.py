from ultralytics import YOLO
import os
import gdown

def load_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'best_model.pt')
    model_path = os.path.abspath(model_path)

    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Starting download from Drive...")
        
        file_id = os.environ.get('MODEL_ID')
        
        if not file_id:
            print("CRITICAL ERROR: 'MODEL_ID' environment variable is missing on Render!")
            return None
            
        try:
            url = f'https://drive.google.com/uc?id={file_id}'
            output = model_path
            gdown.download(url, output, quiet=False)
            
            if not os.path.exists(model_path):
                print("Error: Download finished but file is missing.")
                return None
                
        except Exception as e:
            print(f"Error downloading model with gdown: {e}")
            return None
    else:
        print(f"Found existing model at {model_path}. Skipping download.")

    try:
        print(f"Loading YOLOv8 model into memory...")
        model = YOLO(model_path)
        
        print("Model loaded successfully!")
        return model
        
    except Exception as e:
        print(f"CRITICAL ERROR loading YOLO model: {e}")
        return None

model = load_model()