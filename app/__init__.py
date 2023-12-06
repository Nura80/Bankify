from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# Create instances of Flask extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_name='development'):
    # Create the Flask application instance
    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object(f'config.{config_name}')

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Enable CORS
    CORS(app)

    # Import blueprints
    from app.users.routes import users_bp
    from app.accounts.routes import accounts_bp

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(accounts_bp)

    return app
