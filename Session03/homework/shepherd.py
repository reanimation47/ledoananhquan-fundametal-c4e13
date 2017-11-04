sheep = [5, 7, 8, 12, 15, 9, 22]

print("These are my sheep's size: ")

print(sheep)

print("Now my biggest sheep has a size of",max(sheep),"lets shear it")

sheep.remove(max(sheep))

sheep.insert(0, 8)

print("After shearing, here are my new flock: ",sheep)

print("After a month, here are my sheep's size: ",[x+50 for x in sheep])
