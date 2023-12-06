import os

class Config:
    # Flask App Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    DEBUG = False
    TESTING = False

    # Database Configuration (Replace with your actual database URI)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bankify.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Set the token expiration time (in seconds)

    # Bcrypt Configuration
    BCRYPT_LOG_ROUNDS = 12

    # CORS Configuration
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    # Example production-specific configurations
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/db_name'
    JWT_SECRET_KEY = 'your_production_jwt_secret_key'

# Define a dictionary to map environment names to their corresponding configurations
config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig
)

# Function to get the configuration based on the environment name
def get_config(env_name):
    return config_by_name.get(env_name, Config)


