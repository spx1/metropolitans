import os
from flask import Flask, Blueprint, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from service import VendorService, CategoryService, ExpenseService
from model import Vendor, Category, Expense
from typing import Tuple, Callable

def get_database_uri() -> str:
    user = os.getenv('SQL_USER')
    key = os.getenv('SQL_KEY')
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    database_uri = f"mariadb+pymysql://{user}:{key}@{server}/{database}?charset=utf8mb4"
    return database_uri

app = Flask(__name__,
            template_folder="templates",
            static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/status",methods=['GET'])
def status():
    return "hello world"

@app.route("/page/main")
def display_main_page():
    return render_template('main.html')

@app.route("/page/vendor")
def display_vendor_page():
    return render_template('vendors.html')

@app.route("/page/expense")
def display_expense_page():
    return render_template('expenses.html')

api_bp = Blueprint('API', __name__)
app.register_blueprint(api_bp, url_prefix='/api/v1')

@api_bp('/vendors',method=["GET"])
def get_vendors():
    return [dict(t) for t in VendorService.get()]

def post_generic(foo, data : dict) -> Tuple[str, int]:
    try:
        foo(data)
        return jsonify({'message': 'Success'}), 200
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"}), 500
    
@api_bp('/vendors',method=["POST"])
def post_vendors():
    return post_generic(VendorService.add, request.get_json())
    
@api_bp('/categories',method=["GET"])
def get_categories():
    return [dict(t) for t in CategoryService.get()]

@api_bp('/categories',method=["POST"])
def post_categories():
    return post_generic(CategoryService.add, request.get_json())

@api_bp('/expenses',method=["GET"])
def get_expenses():
    return [dict(t) for t in ExpenseService.get()]

@api_bp('/expenses',method=["POST"])
def post_expenses():
    return post_generic(ExpenseService.add, request.get_json())