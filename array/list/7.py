a =[[[0 for k in range(2)] for j in range(2)] for i in range(2)]

for i in range(2):
    for j in range(2):
        for k in range(2):
            a[i][j][k] = input("Enter the value of a ")

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(a[i][j][k])
