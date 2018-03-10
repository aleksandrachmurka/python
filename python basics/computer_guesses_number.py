#Ćwiczenia Pythona "Pyton dla każdego" M. Dawson


#computer guesses a number
import random
print("Hi, let me try to guess a number you picked")
number = int(input("Pick a number from 1 to 100:"))
guess = random.randint(1, 100)
count = 0
while number != guess:
    if number>guess:
        print(guess)
        print("Too small!")
        guess = random.randint(1, 100)
    else:
        print(guess)
        print("Too big!")
        guess = random.randint(1, 100)
    count += 1
print(guess)
print("I guessed! It took me " + str(count) + " tries.")

input("\n\nTo exit press Enter.")
