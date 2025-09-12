import app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship

class Vendor(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    vendorname = app.db.Column(app.db.String(50), nullable=False)
    contactname = app.db.Column(app.db.String(50))
    contactphone = app.db.Column(app.db.String(15))
    email = app.db.Column(app.db.String(80))
    address = app.db.Column(app.db.String(100))
    comments = app.db.Column(app.db.Text)
    created = app.db.Column(app.db.Date, nullable=False)
    updated = app.db.Column(app.db.Date, nullable=False)

class Category(app.app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    categoryname = app.db.Column(app.db.String(50), nullable=False)
    is_deprecated = app.db.Column(app.db.Boolean, nullable=False)
    created = app.db.Column(app.db.Date, nullable=False)
    updated = app.db.Column(app.db.Date, nullable=False)

class Expense(app.app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    vendor_id = mapped_column(ForeignKey("vendor.id"))
    vendor = relationship("Vendor")
    created = app.db.Column(app.db.Date, nullable=False)
    updated = app.db.Column(app.db.Date, nullable=False)
    amount = app.db.Column(app.db.Numeric(precision=10, scale=2), nullable=False)
    is_recurring = app.db.Column(app.db.Boolean, nullable=False)
    category_id = mapped_column(ForeignKey("category.id"))
    category = relationship("Category")


