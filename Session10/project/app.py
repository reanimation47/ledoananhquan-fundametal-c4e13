from flask import Flask, render_template, request, flash
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '.XG7HzSs/4LVEn[8' #. XBOX GOLF 7 HULU zip SKYPE skype / 4 LAPTOP VISA EGG nut [ 8

#1.Connect to data base
mlab.connect()

#2.Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

# 3.Try insertng an item
# tv = Item(
#     title='Cát y sét cũ và đắt',
#     image= "https://cdn1.tgdd.vn/Files/2015/09/26/708646/bi-kip-chon-mua-tivi-cu-1.jpg",
#     description= 'Cát sét cũ cũ nên đắt',
#     price= 300000000
# )
#
# tv.save()

# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)



@app.route('/')
def index():
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
    items = Item.objects()
    return render_template('index.html', items=items)

@app.route('/admin')
def admin():
    return render_template('admin.html',items = Item.objects())

@app.route('/edit_item/<item_id>',methods = ['GET','POST'])
def edit_item(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET' :
        return render_template('edit_item.html', item=item)
    elif request.method == 'POST':
        form = request.form
        title = form['title']
        description = form['description']
        image = form['image']
        price = form['price']

        item.update(title=title,description=description,image=image,price=price)

        flash('Done')

        return render_template('edit_item.html', item=Item.objects().with_id(item_id))

@app.route('/item_delete/<item_id>',methods = ['GET','POST','DELETE'])
def item_delete(item_id):
    item = Item.objects().with_id(item_id)
    if request.method == 'GET':
        return render_template('delete_item.html')
    elif request.method == 'POST':
        form = request.form


        item.update(title={},description={},image={},price={},_id={})

        return render_template('admin.html')

#
# @app.route('/delete/<item_id>')
# def delete(item_id):
#     DELETE /databases/oldstuff/collections/item/item_id


if __name__ == '__main__':
  app.run(debug=True)
