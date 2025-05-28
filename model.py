from .app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendorname = db.Column(db.String(50), nullable=False)
    contactname = db.Column(db.String(50))
    contactphone = db.Column(db.String(15))
    email = db.Column(db.String(80))
    address = db.Column(db.String(100))
    comments = db.Column(db.Text)
    created = db.Column(db.Date, nullable=False)
    updated = db.Column(db.Date, nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(50), nullable=False)
    is_deprecated = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.Date, nullable=False)
    updated = db.Column(db.Date, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = mapped_column(ForeignKey("vendor.id"))
    vendor = relationship("Vendor")
    created = db.Column(db.Date, nullable=False)
    updated = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    is_recurring = db.Column(db.Boolean, nullable=False)
    category_id = mapped_column(ForeignKey("category.id"))
    category = relationship("Category")


