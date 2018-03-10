#Ćwiczenia z Pythona "Python dla każdego" M. Dawson


#Hangman
import random

HANGMAN = (
    """
    -------
    |     |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -------
    |     |
    |     0
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
 -------
    |     |
    |     0
    |    -+-
    |
    |
    |
    |
    |
    -----------
    """,
     """
 -------
    |     |
    |     0
    |   /-+-
    |
    |
    |
    |
    |
    -----------
    """,
     """
 -------
    |     |
    |     0
    |   /-+-/
    |
    |
    |
    |
    |
    -----------
    """,
    """
 -------
    |     |
    |     0
    |   /-+-/
    |     |
    |
    |
    |
    |
    -----------
    """,
    """
 -------
    |     |
    |     0
    |   /-+-/
    |     |
    |     |
    |    |
    |    |
    |
    -----------
    """,
   """
 -------
    |     |
    |     0
    |   /-+-/
    |     |
    |     |
    |    | |
    |    | |
    |
    -----------
    """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("PYTHON", "POPELINA", "RUMSZTYK", "KOT", "ROMINA", "KOCINA", "MISIO")
word = random.choice(WORDS)
so_far = " _ " * len(word)
wrong = 0
used = []
print("SZUBIENICA Welcome and good luck")
print("Guess a word from: PYTHON, POPELINA, RUMSZTYK, KOT, ROMINA, KOCINA, MISIO")


while wrong < MAX_WRONG and so_far != word:
	print(HANGMAN[wrong])
	print("\nWykorzystałeś już następujące litery:\n", used)
	print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

	guess = input("\n\nWprowadź literę: ")
	guess = guess.upper()
    
	while guess in used:
	    print("Już wykorzystałeś literę", guess)
	    guess = input("Wprowadź literę: ")
	    guess = guess.upper()

	used.append(guess)

	if guess in word:
	    print("\nTak!", guess, "znajduje się w zagadkowym słowie!")
	    new = ""
	    for i in range(len(word)):
	    	if guess == word[i]:
	    	    new += guess
    		else:
                    new += so_far[i]
                so_far = new
	else:
            print("\nNiestety literka nie wystepuje w slowie")
		
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\n Wisisz")
else:
    print("\nNie wisisz")

print("\n Słowo to:", word)

 

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
