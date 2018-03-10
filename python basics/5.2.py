#Ćwiczenia z Pythona "Python dla każdego" M. Dawson

#kreator postaci

character = {"siła": 0, "zdrowie": 0, "mądrość": 0, "zręczność": 0}
values = int(character["siła"] + character["zdrowie"] + character["mądrość"] + character["zręczność"])


choice = None
while choice != "0":
    print(
        """
            Kreator postaci
            0 - zakończ
            1 - wyświetl punkty
            2 - dodaj punkty
            3 - odejmij punkty
        """
        )
    choice = input("Wybierz:")
    print()
    
    if choice == "0":
        print("Pa")
        
    elif choice == "1":
        print(character.items())
        
    elif choice == "2":
        if values >= 30:
            print("Nie możesz dodawać więcej punktów")
            break
        else:
            key = input("Jakie punkty dodać?:")
            if key in character:
                value = int(input("Podaj ilość punktów:"))
                if (values+value) >= 30:
                    print("Nie możesz dodać aż tylu punktów")
                else:
                    character[key] += value
                
    elif choice == "3":
        key = input("Jakie punkty odjąć?:")
        if key in character:
            value = int(input("Podaj ilość punktów:"))
            character[key] -= value
            
    values = int(character["siła"] + character["zdrowie"] + character["mądrość"] + character["zręczność"])
    print("Twój bohater zdobywa kolejne punkty")
    print("Ma ich łącznie:", values)
    

  
          
    




    
    
 
