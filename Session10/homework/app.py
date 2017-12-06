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
    des1 = StringField()
    des2 = StringField()
    price1 = IntField()
    price2 = IntField()

# # 3.Try insertng an item
# tv = Item(
#     title='Muốn cùng chúng tôi giữ gìn hạnh phúc gia đình?',
#     image= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiSSXd5EFIYoZ7-RvW3mUTXeAqgvtQBpsBtuYWdLhFFCaIWHlQRw",
#     des1= 'Yêu cầu đang đi học đại học hoặc đã đi làm',
#     des2= 'Liên hệ',
#     price1= 350000,
#     price2= 500000,
# )



# items = Item.objects()
# for item in items:
#     print(item.title)
#     print(item.price)


@app.route('/')
def homepage():
    data = Item.objects()
    return render_template('p_t_meeting.html', items=data)

if __name__ == '__main__':
  app.run(debug=True)
