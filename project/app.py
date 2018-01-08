from flask import *
import mlab
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '.XG7HzSs/4LVEn[8' #. XBOX GOLF 7 HULU zip SKYPE skype / 4 LAPTOP VISA EGG nut [ 8

#1. Connect to database
mlab.connect()

#2. Design collection
class Item(Document):
    title = StringField()
    image = StringField()
    description = StringField()
    price = IntField()

class User(Document):
    username = StringField()
    password = StringField()

thao = User(username='thao', password='thaoadmin')
thao.save


@app.route('/')
def index():
    items = Item.objects() # Get ALL items
    loggedin = session.get('loggedin', False)
    return render_template('index.html', items=items, loggedin=loggedin)

@app.route('/add_item', methods=['GET','POST'])
def add_item():
    if request.method == 'GET':
        return render_template('add_item.html')
    elif request.method == 'POST': #receive form
        #1 extract data in form
        form = request.form
        title = form['title']
        image = form['image']
        description = form['description']
        price = form['price']

        #2 add into database
        new_item = Item(title=title,image=image,description=description,price=price)
        new_item.save()  #3 save into database

        return "Ok anh"

@app.route('/admin')
def admin():
    if session.get('loggedin', False) :
        return render_template('admin.html', items=Item.objects())
    else:
        return redirect( url_for('admin'))

@app.route('/edit_item/<item_id>', methods=['GET','POST'])
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
        flash('X')

        return render_template('edit_item.html', item=Item.objects().with_id(item_id))

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        user = user.objects(username=username).first()
        if user is None :
            return 'Username or password is incorrect'
        elif user.password != password:
            return 'Username or password is incorrect'
        else:
            session['loggedin'] = True
            return redirect(url_for('admin'))


@app.route('/logout')
def logout():
    session['loggedin'] = False
    return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)
