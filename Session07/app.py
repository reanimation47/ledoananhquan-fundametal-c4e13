from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return "Hello C4E13"
#
# @app.route('/hello/tuananh')
# def hello_me():
#     return "Hello Huy"
#
# @app.route('/<lastname>/<firstname>')
# def hello(lastname, firstname):
#     return "Hello " + lastname + " " + firstname
#
# @app.route('/sum/<int:x>/<int:y>')
# def sum(x, y):
#
#     m = x + y
#     m = str(m)
#     return m

if __name__ == '__main__':
  app.run(debug=True)
