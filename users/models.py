from mongoengine import Document, StringField, BooleanField, ImageField

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_farmer = BooleanField(default=True)
    location = StringField()
    phone = StringField()
    profile_picture = StringField()  
