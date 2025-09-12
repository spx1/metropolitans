from flask import Flask, Blueprint, render_template, jsonify, request
import service
from typing import Tuple, Callable

app_bp = Blueprint('Application', __name__)
api_bp = Blueprint('API', __name__)

@app_bp.route("/status",methods=['GET'])
def status():
    return "hello world"

@app_bp.route("/page/main")
def display_main_page():
    return render_template('main.html')

@app_bp.route("/page/vendor")
def display_vendor_page():
    return render_template('vendors.html')

@app_bp.route("/page/expense")
def display_expense_page():
    return render_template('expenses.html')

@api_bp('/vendors',method=["GET"])
def get_vendors():
    return [dict(t) for t in service.VendorService.get()]

def post_generic(foo, data : dict) -> Tuple[str, int]:
    try:
        foo(data)
        return jsonify({'message': 'Success'}), 200
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"}), 500
    
@api_bp('/vendors',method=["POST"])
def post_vendors():
    return post_generic(service.VendorService.add, request.get_json())
    
@api_bp('/categories',method=["GET"])
def get_categories():
    return [dict(t) for t in service.CategoryService.get()]

@api_bp('/categories',method=["POST"])
def post_categories():
    return post_generic(service.CategoryService.add, request.get_json())

@api_bp('/expenses',method=["GET"])
def get_expenses():
    return [dict(t) for t in service.ExpenseService.get()]

@api_bp('/expenses',method=["POST"])
def post_expenses():
    return post_generic(service.ExpenseService.add, request.get_json())