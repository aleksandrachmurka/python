#Ćwiczenia Pythona "Pyton dla każdego" M. Dawson


#powitanie motywacyjne
name = input("Kto dzisiaj wymiata w Pythona?")
print("Jasne,że ", name.upper(), "!")
#print("\a")

#wyliczmy napiwek
suma = int(input("Na ile PLN opiewa rachunek?"))
print("\nJeśli obsługa była na dobrym poziomie, dodajmy do tego napiwek w wysokości:" , suma * 0.15)
print("\nJeśli obsługa była wyjątkowa, dodajmy do tego napiwek w wysokości:" , suma * 0.2)

#odgadnij liczbę
import random
print("Hej, odgadnij liczbę")
number = random.randint(1, 100)
guess = int(input("Podaj liczbę od 1 do 100:"))
count = 0
while guess != number:
    if guess>number:
        print("Too big!")
    else:
        print("Too small!")
    count += 1
    guess = int(input("Spróbuj jeszcze raz"))
print("Gratulacje, odgadłeś liczbę! Potrzebne było do tego " + str(count) + "prób.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
