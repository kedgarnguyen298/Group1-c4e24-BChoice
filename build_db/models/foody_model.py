from mongoengine import *

class Foody(Document):
    title = StringField()
    name = StringField()
    address = StringField()
    address_search = StringField()
    image = URLField()
    rate = IntField()
    position = DictField()