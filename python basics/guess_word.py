#ENG guess a word
import random

WORDS = ("apple", "banana", "cherry", "chocolate", "donut", "peach", "wine")
word = random.choice(WORDS)
print("Guess what I picked for you. I could choose from: apple, banana, cherry, chocolate, donut, peach, wine.")
print("Word has " + str(len(word)) + " letters")
count = 0

while count < 6:
    letter = input("Is this letter in a word?")
    if letter in word:
        print("Yes, this letter is in the word")
    else:
        print("No, this letter is not in the word")
    count += 1
guess = input("Try to guess!")

if guess == word:
    print("Congrats! You guessed!")
else:
    print("Not this time!")





