#PL ogdadujemy słowo
import random

WORDS = ("python", "jedna", "rzecz", "dobra", "linux", "windows", "wino")
word = random.choice(WORDS)
print("Słowo ma" + str(len(word)) +" liter")
count = 0

while count < 6:
    letter = input("Czy w słowie znajduje się litera?")
    if letter in word:
        print("Ta litera znajduje się  słowie")
    else:
        print("W słowie nie ma takiej litery")
    count += 1
guess = input("Podaj słowo")

if guess == word:
    print("Gratulacje! Odgadłeś!")
else:
    print("Niestety nie tym razem!")





