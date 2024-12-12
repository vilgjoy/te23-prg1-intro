import random
import time

my_list = [42, 'hej', 3.14, True, [1,2,3], {"key": "value"}]
rundor = 5
nu_rund = 0

while True:
    random_item = random.choice(my_list)
    print("Spelet startar nu!")

    starta_tid = time.time()
    for sak in range(len(my_list)):
        gissa = input(f"Vad är datatypen på [{random_item}]? ").strip().lower()
        if gissa == type(random_item).__name__.lower():
            sluta_tid = time.time()
            hur_många = round(sluta_tid - starta_tid, 2)
            print(f"Korrekt. Du gissade rätt på datatypen på {hur_många} seconds.")
            break
        else:
            print("Fel, försök igen")
    
    kör_igen = input("Vill du köra igen? ")
    if kör_igen != "ja":
        print("Loser...")
        break
    

