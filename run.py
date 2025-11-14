from flask import Flask, render_template
from flask_cors import CORS
import os

def create_app():
    template_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'template')
    static_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'statics')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')
    
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    from backend.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)