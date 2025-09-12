from typing import TypedDict, Required
from datetime import datetime as dt

class IVendor(TypedDict, total=False):
    id : int
    vendorname : Required[str]
    contactname : str
    contactphone : str
    email : str
    address : str
    comments : str

