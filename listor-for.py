from random import choice
inventory = {
    "Pizza": {"beskrivning": "Italian, 20 minuter", "kvantitet": 5},
    "Pasta": {"beskrivning": "Italian, 20 minuter", "kvantitet": 3}
}

run = True
while run:
    choice = input("Vad vill du ha? \n[1] Skriva ut\n[2] Lägga in dish\n[3] Avsluta\n[4] Ta bort dish\n[5] Uppdatera kvantitet:")
    if choice == "3":
        print("Avslutar")
        run = False
    elif choice == "2":
        new_dish = input("Vilken dish vill du lägga in?: ")
        if new_dish in inventory:
            print(f"{new_dish} finns redan")
        else:
            beskrivning = input(f"Skriv en beskrivning eller typ för {new_dish}: ")
            kvantitet = int(input(f"Skriv hur många {new_dish} som finns: "))
            inventory[new_dish] = {"beskrivning": beskrivning, "kvantitet": kvantitet} #Lägga till dish med sin beskrivning till dict
            print(f"{new_dish} har lagts till i listan")
    elif choice == "1":
        if inventory:
            print("\nHär är varje dish:")
            for dish, details in inventory.items():
                print(f"{dish}: {details['beskrivning']} /\ Kvantitet: {details['kvantitet']}")
        else:
            print("Finns inga dishes kvar")
        run = False

    elif choice == "4":
        if inventory:
            print("\nHär är varje dish:")
            for dish in inventory:
                print(f"- {dish}")
            remove_dish = input("Vilken dish vill du ta bort?: ")

            # Om dishen är i listan
            if remove_dish in inventory:
                inventory.pop(remove_dish) # Ta bort en dish med dens namn
                print(f"{remove_dish} har tagits bort")
            else:
                print(f"{remove_dish} exiisterar inte i listan")
        else:
            print("Finns inga dishes kvar")
    elif choice == "5":
        if inventory:
            print("\nHär finns varje dish:")
            for dish in inventory:
                print(f"- {dish}")
            uppdatera_dish = input("Skriv namnet på din dish som du vill höja kvantiteten på: ")

            if uppdatera_dish in inventory:
                ny_kvantitet = int(input(f"Skriv din nya kvantitet för {uppdatera_dish}: "))
                inventory[uppdatera_dish]["kvantitet"] = ny_kvantitet
            else:
                print(f"{uppdatera_dish} finns inte i listan")

    else:
        print("Välj ett av nummerna [1], [2], [3], [4] eller [5]: ")
        