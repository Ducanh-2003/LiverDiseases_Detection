from flask import Flask, render_template
import os

def create_app():
    template_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'template')
    static_dir = os.path.join(os.path.dirname(__file__), 'frontend', 'statics')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')

    @app.route('/')
    def index():
        return render_template('index.html')

    from backend.api.routes import api_bp
    app.register_blueprint(api_bp)

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)