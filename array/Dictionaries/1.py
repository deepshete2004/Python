a = {"Name":"Deep",
     "Age":22,
     "Year":2004,
     "Gender":"Male",
     "City":"Ahmedabad",
     "Country":"India",
     "colors":["red","white","blue"]
    }

print(a['Name'])

print(len(a))

a['Age']=20

b = a.copy()

#del a

#a.clear()

for i in a:
    print(a[i])

for x,y in a.items():
    print(x,y)

    
