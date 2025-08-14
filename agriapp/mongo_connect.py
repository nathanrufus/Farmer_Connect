import mongoengine
from decouple import config

mongoengine.connect(
    db=config('MONGO_DB_NAME', default='farmer_connect'),
    host=config('MONGO_HOST', default='localhost'),
    port=int(config('MONGO_PORT', default=27017)),
    alias='default'  # 🔑 THIS IS REQUIRED
)
