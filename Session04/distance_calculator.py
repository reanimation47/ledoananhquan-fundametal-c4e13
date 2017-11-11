from haversine import haversine

Hanoi = {
    'name': 'Hanoi',
    'hnlat': 21.0277644,
    'hnlng': 105.83415979999995,
}
Danang = {
    'name': 'Danang',
    'dnlat': 16.0544068,
    'dnlng': 108.20216670000002,
}
Hochiminh = {
    'name': 'Hochiminh',
    'hcmlat': 10.8230989,
    'hcmlng': 106.6296638,
}
Hue = {
    'name': 'Hue',
    'hlat': 16.4498,
    'hlng':107.5623501,
}
# hnlat = input("Hanoi's latitude : ")
# hnlng = input("Hanoi's longtitude : ")
#
# dnlat = input("Danang's latitude : ")
# dnlng = input("Danang's longtitude : ")
cities = [
    {
        'name': 'Hanoi',
        'hnlat': 21.0277644,
        'hnlng': 105.83415979999995,
    },
    {
        'name': 'Danang',
        'dnlat': 16.0544068,
        'dnlng': 108.20216670000002,
    },
    {
        'name': 'Hochiminh',
        'hcmlat': 10.8230989,
        'hcmlng': 106.6296638,
    },
    {
        'name': 'Hue',
        'hlat': 16.4498,
        'hlng':107.5623501,
    }
]

city1 = cities[0]
city2 = cities[1]
city3 = cities[2]
city4 = cities[3]

Hanoi_co = (city1['hnlat'],city1['hnlng'])
Danang_co = (city2['dnlat'],city2['dnlng'])
Hochiminh_co = (city3['hcmlat'],city3['hcmlng'])
Hue_co = (city4['hlat'],city4['hlng'])

list = [Hanoi_co, Danang_co, Hochiminh_co, Hue_co]
listx = ['Hanoi', 'Danang', 'Hochiminh', 'Hue']

for i in range(len(list)-1):
    for j in range(i +1,len(list)):
        q = haversine(list[i],list[j])
        print("Distance between {0} and {1} is {2}".format(listx[i],listx[j],q))
