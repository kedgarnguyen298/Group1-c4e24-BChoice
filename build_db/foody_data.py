import json
import mlab
from models.foody_model import Foody
from random import randint
from decode_test import no_accent_vietnamese

# if __name__ == "__main__":    
mlab.connect()

    # 1. Read data
with open('foody_data.json', 'r', encoding='utf8') as f:
    data = f.read()

obj = json.loads(data)

food_items = obj['reply']['delivery_infos']

for item in food_items:
    name = item['name']
    address = item['address']
    image = item['photos'][6]['value']
    rate = randint(8, 10)
<<<<<<< HEAD
    title = "Bữa chính"
=======
    title = "Ăn vặt"
>>>>>>> 8992a84e9ea451bd61564f5d442122c8e1d3ab92
    address_search = no_accent_vietnamese(address.lower())
    #2. Push into DB
    new_item = Foody(name=name, address=address, image=image, rate=rate, title=title, address_search=address_search)
    new_item.save()







