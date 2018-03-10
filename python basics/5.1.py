#Ćwiczenia zh "Python dla każdego" M. Dawson


#wyświetlić wszystkie elementy list w losowej kolejności, bez powtarzania
from random import randint
words = ["adam", "beata", "celina", "danuta", "ewa", "florian", "gerwazy", "henryk"]
used = []
count = 0
    
 
while count < len(words):
    x = randint(0,len(words) - 1)
    record = words[x]
    if record not in used:
        print(record)
        used.append(record)
        count=+1
    else:
        pass
    
    
       
