from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from .models import Student

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student