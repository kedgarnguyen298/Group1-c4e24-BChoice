import mongoengine
import mlab
from models.foody_model import Foody

if __name__ == "__main__":    
    mlab.connect()

    Foody.objects.delete()