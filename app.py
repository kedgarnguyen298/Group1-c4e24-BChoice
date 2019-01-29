from flask import Flask, render_template, redirect, request
from build_db import mlab
from build_db.models.foody_model import Foody
from random import randint

mlab.connect()
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/food-expect', methods = ["GET", "POST"])
def expect():
  if request.method == "GET": 
    return render_template("expect.html")
  elif request.method == "POST":
    form = request.form
    user_address = form["address"]
    user_title = form["title"]
    
    return redirect('/food-suggest/' + user_title + '/' + user_address)
     
@app.route('/food-suggest/<user_title>/<user_address>', methods = ["GET"])
def suggest(user_title, user_address):
  item_list = Foody.objects(title = user_title)

  x = randint(0, len(item_list))
  y = randint(0, len(item_list))
  while y == x:
    y = randint(0, len(item_list))
  z = randint(0, len(item_list))
  while (z == x) or (z == y):
    z = randint(0, len(item_list))
  
  show_name1 = item_list[x]['name']
  show_address1 = item_list[x]['address']
  show_image1 = item_list[x]['image']
  show_rate1 = item_list[x]['rate']

  show_name2 = item_list[y]['name']
  show_address2 = item_list[y]['address']
  show_image2 = item_list[y]['image']
  show_rate2 = item_list[y]['rate']

  show_name3 = item_list[z]['name']
  show_address3 = item_list[z]['address']
  show_image3 = item_list[z]['image']
  show_rate3 = item_list[z]['rate']
  
  return render_template("suggest.html", show_name1=show_name1, show_name2=show_name2, show_name3=show_name3,
                                             show_address1=show_address1, show_address2=show_address2, show_address3=show_address3,
                                             show_image1=show_image1, show_image2=show_image2, show_image3=show_image3,
                                             show_rate1=show_rate1, show_rate2=show_rate2, show_rate3=show_rate3) 

if __name__ == '__main__':
  app.run(debug=True)