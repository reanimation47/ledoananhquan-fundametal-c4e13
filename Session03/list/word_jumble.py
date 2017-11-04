from random import choice

s = "Hell"

characters = list(s)

word = choice(characters)

menu =[characters]

if word in menu :
    menu.remove(word)
    



print(menu)
