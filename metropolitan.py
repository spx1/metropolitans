import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def get_database_uri() -> str:
    user = os.getenv('SQL_USER')
    key = os.getenv('SQL_KEY')
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    database_uri = f"mariadb+pymysql://{user}:{key}@{server}/{database}?charset=utf8mb4"
    return database_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)