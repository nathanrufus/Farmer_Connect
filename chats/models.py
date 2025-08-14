from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField
from users.models import User
from datetime import datetime

class Message(Document):
    sender = ReferenceField(User)
    receiver = ReferenceField(User)
    message = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    is_read = BooleanField(default=False)
