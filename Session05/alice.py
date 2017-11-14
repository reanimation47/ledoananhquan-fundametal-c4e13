alice_file = open('alice.txt')
text = alice_file.read() #read whole file
alice_file.close()

ignore_words = ["\n",",",".","?","!","''"]
for ignore_word in ignore_words:
    text = text.replace(ignore_word,"")

words = text.split()


# words = ['alice', 'in','wonderland','about','in','alice']

word_count = {}

for word in words:
    if word not in word_count:
        word_count[word]= 1
    else:
        word_count[word] += 1

print(word_count)
