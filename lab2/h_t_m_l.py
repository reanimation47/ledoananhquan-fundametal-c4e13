from gmail import GMail, Message

from random import choice

file_names= ['1.html','2.html','3.html']

file_names = choice(file_names)
reasons = ['Ebola','đau bụng','đau đầu','gấu bò']
reason = choice(reasons)
template_file = open(file_names)
html_content = template_file.read()
template_file.close()
html_content = html_content.replace('{{reason}}',reason)

gmail = GMail('reanimation151106@gmail.com',\
               'NHATNAm7894')
msg = Message('Hello',\
               to = 'c4e13.lab.huynq@gmail.com',\
               html = html_content)
gmail.send(msg)
# gmail = GMail('reanimation151106@gmail.com','NHATNAm7894')
#
#
#
# msg = Message('Test Message',to='c4e13.lab.huynq@gmail.com',text= 'Hello',html="<b>Hello</b>")
# msg.replace('Hello',msg[mm])
# gmail.send(msg)
