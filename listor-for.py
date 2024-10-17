dishes = ["Pizza", "Pasta"]

run = True
while run:
    choice = input("Vad vill du ha? \n[1] Skriva ut\n[2] Lägga in dish\n[3] Avsluta\n[4] Ta bort dish\n:")
    if choice == "3":
        print("Avslutar")
        run = False
    elif choice == "2":
        new_dish = input("Vilken dish vill du lägga in?: ")
        dishes.append(new_dish)
        print(f"{new_dish} har lagts till i listan")
    elif choice == "1":
        if dishes:
            print("\nHär är varje dish:")
            for dish in dishes:
                print(f"- {dish}")
        else:
            print("Finns inga dishes kvar")
        run = False

    elif choice == "4":
        if dishes:
            print("\nHär är varje dish:")
            for dish in dishes:
                print(f"- {dish}")
            remove_dish = input("Vilken dish vill du ta bort?: ")

            # Om dishen är i listan
            if remove_dish in dishes:
                dishes.remove(remove_dish) # Ta bort en dish med dens namn
                print(f"{remove_dish} har tagits bort")
            else:
                print(f"{remove_dish} exiisterar inte i listan")
        else:
            print("Finns inga dishes kvar")
    else:
        print("Välj ett av nummerna [1], [2], [3] or [4]: ")
        