lista = [] #üres lista

lista.append("Fifa")
lista.append("GTA")
lista.append("COD")
lista.append("LOL")
lista.append("For Honor")
lista.append("PUBG")
lista.append("Yandere Simulator")

#kiiratás 3 féle képpen
#1.
print(lista)

#2.
for item in lista:
    print(item)
print("************************************************")

#3.
#len a lista hossza (hány elemet tartalamz)
for i in range(len(lista)):
    print(lista[i])

#szűrés 
for item in lista:
    if item == "COD":
        print("IGEN")
    else:
        print("NO")

