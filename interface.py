from typing import TypedDict
from datetime import datetime as dt

class IVendor(TypedDict):
    id : int
    vendorname : str
    contactname : str
    contactphone : str
    email : str
    address : str
    comments : str
    created : dt
    updated : dt

