
from pydantic import BaseModel
import re

class LoginRequestDto(BaseModel):
     msisdn : str



     # Class method for validation
     @classmethod
     def validate_format(cls, value):
         if not re.match(r"^\+?\d+$", value):
             raise ValueError("MSISDN must contain only digits with optional '+'")

         if len(value) not in [11, 13]:
             raise ValueError("MSISDN must be 11 digits (local) or 13 digits (international)")

         return value