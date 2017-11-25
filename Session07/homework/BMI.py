from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:x>/<float:y>')
def bmi(x, y):
    bmi = x / (y**2)
    if bmi < 16 :
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run( debug=True)
