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

class ICategory(TypedDict, total=False):
    id : int
    categoryname : Required[str]
    is_deprecated : bool

