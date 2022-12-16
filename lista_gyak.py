mobilok = ["iPhone 6S", "Samsung Galaxy A80", "Xiaomi 11", "Nokia Lumia 620"]
print(mobilok)

for item in mobilok: 
    print(item)
print("*********************")

mobilok.append("Alacatel OneTouch POP") 
mobilok.pop(0)
mobilok.pop(1)
mobilok.clear()

for i in range(len(mobilok)):
    print(mobilok[i])

