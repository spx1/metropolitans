from .metropolitan import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendorname = db.Column(db.String(50), nullable=False)
    contactname = db.Column(db.String(50))
    contactphone = db.Column(db.String(15))
    email = db.Column(db.String(80))
    address = db.Column(db.String(100))
    comments = db.Column(db.Text)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = mapped_column(ForeignKey("vendor.id"))
    created = db.Column(db.Date)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    is_recurring = db.Column(db.Boolean, nullable=False)
    category = db.Column(db.String(80), nullable=False)

