import mongoengine
import mlab
from models.foody_model import Foody

mlab.connect()

Foody.objects.update(title = "Bữa chính")