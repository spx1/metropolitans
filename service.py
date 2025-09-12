from model import Vendor
from interface import IVendor
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