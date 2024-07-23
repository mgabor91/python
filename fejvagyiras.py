print("Üdvözöllek a fej vagy írás játékomban!")
      
while True:
    try:
        ertek = input("Kérlek gépeld be a tipped (fej, írás): ")
    except ValueError:
        print("Csak a fej vagy írás szöveget fogadom el")
        continue
    if ertek == "fej" or ertek == "írás":
        break
    else:
        print('Csak a fej vagy írás szöveget fogadom el')

import random
fejvagyiras = random.randint(0,1)

if fejvagyiras == 0:
        fejvagyiras = "fej"
else:
        fejvagyiras = "írás"

if fejvagyiras == ertek:
        print("Nyertél,", fejvagyiras ,"volt")
else: 
      print("Vesztettél,", fejvagyiras ,"volt")
