from flask import Flask, render_template, redirect, request
from build_db import mlab
from build_db.models.foody_model import Foody

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
    return redirect('/food-suggest/<user_title>/<user_address>'), user_address, user_title
     
@app.route('/food-suggest/<user_title>/<user_address>', methods = ["GET"])
def suggest(user_title, user_address):
  item_list = Foody.objects()
  for item in item_list:
    name = item["name"]
    address = item["address"]
    image = item["image"]
    rate = item["rate"]
    latitude = item["position"]["latitude"]
    longitude = item["position"]["latitude"]
    title = item["title"]
    if title == user_title:
      show_name = name
      show_address = address
      show_image = image
      show_rate = rate
      return render_template("suggest.html", show_name=show_name,
                                             show_address=show_address,
                                             show_image=show_image,
                                             show_rate=show_rate)  
@app.route('/img')
def img():
  return render_template('jkasd.html')

if __name__ == '__main__':
  app.run(debug=True)