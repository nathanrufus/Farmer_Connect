from mongoengine import Document, StringField, ReferenceField, DateTimeField
from users.models import User
from datetime import datetime

class Article(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(User)
    image = StringField()  # URL/path
    posted_on = DateTimeField(default=datetime.utcnow)
