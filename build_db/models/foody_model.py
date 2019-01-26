from mongoengine import *

class Foody(Document):
    title = StringField()
    name = StringField()
    address = StringField()
    image = URLField()
    rate = IntField()
    position = DictField()