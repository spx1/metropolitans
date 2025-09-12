from model import Vendor, Category, Expense
from interface import IVendor, ICategory, IExpense
from app import db
from typing import List
import datetime

class InvalidInputException(BaseException):
    pass

class OperationFailed(BaseException):
    pass

class VendorService:
    @staticmethod
    def get() -> List[Vendor]:
        vendors : List[Vendor] = db.session.query(Vendor).order_by('vendorname').all()
        return vendors

    @staticmethod
    def add(vendor_data : IVendor):
        def is_vendor_taken(vendor_name) -> bool:
            return db.session.query(Vendor).filter(Vendor.name == vendor_name).count() > 0
        
        def validate_input(vd : IVendor) -> bool:
            if vd is None:
                raise InvalidInputException("No IVendor object passed to VendorService.add")
            if not vd["vendorname"]:
                raise InvalidInputException("Required field 'vendorname' is not specified")
            if is_vendor_taken(vd['vendorname']):
                raise InvalidInputException(f"Vendor '{vendor_data.vendorname}' already exists")

        current_time = datetime.now()  
        vendor = Vendor(
            vendorname=vendor_data['vendorname'],
            contactname=vendor_data.get('contactname', ""),
            contactphone=vendor_data.get('contactphone',""),
            email=vendor_data.get('email',""),
            address=vendor_data.get('address',""),
            comments=vendor_data.get('comments',""),
            created = current_time,
            updated = current_time
        )
        try:
            db.session.add(vendor)
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def update(id, updated_data : IVendor):
        vendor = db.session.query(Vendor).filter(Vendor.id == id).one()
        if "vendorname" in updated_data: 
            if db.session.query(Vendor).filter(Vendor.vendorname == updated_date["vendorname"]).count() == 0
                vendor.vendorname = updated_data["vendorname"]
        for field in ["contactname","contactphone","email","address","comments"]:
            if field in updated_data:
                vendor.__setattr__(field, updated_data[field])
        db.session.commit()

    @staticmethod
    def delete(id):
        vendor = db.session.query(Vendor).filter(Vendor.id == id).one()
        try:
            db.session.delete(vendor)
            db.session.commit()
        except:
            db.session.rollback()

class CategoryService:
    @staticmethod
    def get() -> List[Category]:
        return db.session.query(Category).all()
    
    @staticmethod
    def add(data : ICategory):
        if not data["categoryname"]:
            raise InvalidInputException("Categoryname must not be an empty string")
        if db.session.query(Category).filter(Category.categoryname == data["categoryname"]).count > 0:
            raise InvalidInputException(f"A category with name '{data["categoryname"]}' already exists")
        
        current_time = datetime.now()
        category = Category(
            categoryname = data["categoryname"],
            is_depricated = data.get("is_deprecated", False),
            created=current_time,
            updated=current_time
        )

        try:
            db.session.add(category)
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def update(id, data : ICategory):
        category = db.session.query(Category).filter(Category.id==id).one()
        category.categoryname = data["categoryname"]
        if "is_deprecated" in data:
            category.is_deprecated = data["is_deprecated"]
        category.updated = datetime.now()

        db.session.commit()

    @staticmethod
    def delete(id):
        category = db.session.query(Category).filter(Category.id==id).one()
        category.is_deprecated = True
        category.updated = datetime.now()

        db.session.commit()

class ExpenseService:
    @staticmethod
    def get():
        return db.session.query(Expense).all()
    
    @staticmethod
    def add(data : IExpense):
        vendor = db.session.query(Vendor).filter(Vendor.id==data["vendor_id"]).one()
        category = db.session.query(Category).filter(Category.id==data["category_id"]).one()

        current_time = datetime.now()
        expense = Expense(
            vendor = vendor,
            category = category,
            created = current_time,
            updated = current_time,
            amount = data["amount"],
            is_recurring = data.get("is_recurring", False)
        )
    
    @staticmethod
    def update(id, data : IExpense):
        expense = db.session.query(Expense).filter(Expense.id==id).one()
        vendor = db.session.query(Vendor).filter(Vendor.id==data["vendor_id"]).one()
        category = db.session.query(Category).filter(Category.id==data["category_id"]).one()

        expense.vendor = vendor
        expense.category = category
        expense.amount = data["amount"]
        if "is_recurring" in data: expense.is_recurring = data["is_recurring"]
        expense.updated = datetime.now()
        db.session.commit()

    @staticmethod
    def delete(id):
        expense = db.session.query(Expense).filter(Expense.id==id).one()
        try:
            db.session.delete(expense)
            db.session.commit()
        except:
            db.session.rollback()

