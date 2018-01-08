from flask import *
from mongoengine import *
import mlab
from geopy import geocoders

app = Flask(__name__)

mlab.connect()

class User(Document):
    username = StringField(required = True, unique = True)
    password = StringField(required=True)

@app.route('/')
def index():
    return render_template('index_test.html')

@app.route('/geocoding-test')
def geocoding():
    return render_template('geocoding_test2.html')

@app.route('/search-test')
def search():
    return render_template('index.html')



@app.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        try:
            new_user = User(username = username, password = password)
            new_user.save()
            return redirect('/')
        except (NotUniqueError):
            return redirect('/sign-up')

if __name__ == '__main__':
  app.run(debug=True)
