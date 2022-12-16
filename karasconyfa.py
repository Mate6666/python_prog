#Feladat: Karácsonyfát rajzolni * karakterekből 
magassag = int(input("Mekkora karacsonyfa legyen?"))
for i in range(magassag):
    for j in range(magassag-i):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()

for i in range(magassag):
    for j in range(10-1):
        print(' ', end=' ')
    print('* * *')

             