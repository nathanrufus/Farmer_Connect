from mongoengine import Document, StringField, FloatField, BooleanField, ReferenceField, DateTimeField
from users.models import User
from datetime import datetime

class Product(Document):
    name = StringField(required=True)
    description = StringField()
    category = StringField()
    price = FloatField(required=True)
    image = StringField()  
    location = StringField()
    is_available = BooleanField(default=True)
    farmer = ReferenceField(User, required=True)
    created_at = DateTimeField(default=datetime.utcnow)
