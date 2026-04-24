import os
from flask import Flask, jsonify
from src.extensions import db, jwt, cors
from src.config import Config
from src.features.auth.login.routes import login_bp
from src.features.auth.signup.routes import signup_bp
from src.features.library.routes import library_bp
from src.features.homepage.routes import homepage_bp
from src.features.research.upload.routes import upload_bp
from src.features.research.published.routes import published_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})

    app.register_blueprint(login_bp,     url_prefix='/api/auth')
    app.register_blueprint(signup_bp,    url_prefix='/api/auth')
    app.register_blueprint(library_bp,   url_prefix='/api/library')
    app.register_blueprint(homepage_bp,  url_prefix='/api/homepage')
    app.register_blueprint(upload_bp,    url_prefix='/api/research')
    app.register_blueprint(published_bp, url_prefix='/api/research')

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'success': False, 'message': 'Not found'}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'success': False, 'message': 'Internal server error'}), 500

    with app.app_context():
        db.create_all()

    return app
