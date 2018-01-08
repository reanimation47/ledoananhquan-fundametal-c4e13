L = [
     #Lat Long của từng người
    ]


lat = []
long = []
for l in L :
  lat.append(l[0])
  long.append(l[1])

print(sum(lat)/len(lat))
print(sum(long)/len(long))
