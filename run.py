from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    
    CORS(app)

    from backend.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)