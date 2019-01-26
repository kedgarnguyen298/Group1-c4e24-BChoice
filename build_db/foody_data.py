import json
import mlab
from models.foody_model import Foody
from random import randint

if __name__ == "__main__":    
    mlab.connect()

    #1. Read data
    with open('foody_data.json', 'r', encoding='utf8') as f:
        data = f.read()
    
    obj = json.loads(data)

    food_items = obj['reply']['delivery_infos']

    for item in food_items:
        name = item['name']
        address = item['address']
        image = item['photos'][6]['value']
        rate = randint(8, 10)
        position = item['position']
        title = "Ăn vặt"
        
        #2. Push into DB
        new_item = Foody(name=name, address=address, image=image, rate=rate, position=position, title=title)
        new_item.save()







