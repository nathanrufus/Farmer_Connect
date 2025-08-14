from mongoengine import Document, StringField, ReferenceField, DateTimeField
from users.models import User
from datetime import datetime

class Discussion(Document):
    topic = StringField(required=True)
    created_by = ReferenceField(User)
    created_at = DateTimeField(default=datetime.utcnow)

class Comment(Document):
    discussion = ReferenceField(Discussion, required=True)
    author = ReferenceField(User)
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
