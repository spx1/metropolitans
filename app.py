import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy


def get_database_uri() -> str:
    user = os.getenv('SQL_USER')
    key = os.getenv('SQL_KEY')
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    database_uri = f"mariadb+pymysql://{user}:{key}@{server}/{database}?charset=utf8mb4"
    return database_uri

def register_routes(app : Flask) -> None:
    from control import app_bp, api_bp
    app.register_blueprint(app_bp, url_prefix='/')
    app.register_blueprint(api_bp, url_prefix='/api/v1')

app = Flask(__name__,
            template_folder="templates",
            static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
register_routes(app)

