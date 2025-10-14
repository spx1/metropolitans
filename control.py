from flask import Flask, Blueprint, render_template, jsonify, request
from service import ExpenseService, CategoryService, VendorService
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

@api_bp.route('/vendors',methods=["GET"])
def get_vendors():
    return [dict(t) for t in VendorService.get()]

def post_generic(foo, data : dict) -> Tuple[str, int]:
    try:
        foo(data)
        return jsonify({'message': 'Success'}), 200
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"}), 500
    
@api_bp.route('/vendors',methods=["POST"])
def post_vendors():
    return post_generic(VendorService.add, request.get_json())
    
@api_bp.route('/categories',methods=["GET"])
def get_categories():
    return [dict(t) for t in CategoryService.get()]

@api_bp.route('/categories',methods=["POST"])
def post_categories():
    return post_generic(CategoryService.add, request.get_json())

@api_bp.route('/expenses',methods=["GET"])
def get_expenses():
    return [dict(t) for t in ExpenseService.get()]

@api_bp.route('/expenses',methods=["POST"])
def post_expenses():
    return post_generic(ExpenseService.add, request.get_json())