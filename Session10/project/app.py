from flask import Flask, render_template
import mlab
from mongoengine import *

app = Flask(__name__)

#1.Connect to data base
mlab.connect()

#2.Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

#3.Try insertng an item
# tv = Item(
#     title='Cát sét cũ và đắt',
#     image= "https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg",
#     description= 'Cát sét cũ cũ nên đắt',
#     price= 3000000
# )

# tv.save()

# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)

@app.route('/')
def index():
    return render_template('index.html',title="TV cũ", image="https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg")

@app.route('/list')
def title_list():
    return render_template('title_for.html', titles=['TV cũ','Cát sét cũ','Người yêu cũ','Máy giặt cũ'])

@app.route('/object')
def object():
    x = {
        'title': 'TV cũ giá cao',
        'image':'https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg',
        'description':'TV vì cũ nên giá cao'
    }

    return render_template('object.html', item=x)

@app.route('/object-list')
def object_list():
    # data = [
    #     {
    #         'title': 'TV cũ',
    #         'image':'http://via.placeholder.com/200x300',
    #         'description': 'TV vì cũ nên đắt',
    #     },
    #     {
    #         'title': 'Cát sét cũ',
    #         'image':'http://via.placeholder.com/200x300',
    #         'description': 'Cát sét vì cũ nên đắt',
    #     },
    # ]
    data = Item.objects()
    return render_template('object_list.html', items=data)

if __name__ == '__main__':
  app.run(debug=True)
