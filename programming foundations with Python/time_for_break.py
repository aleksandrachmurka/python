# from Udacity course "Programming Foundations with Python"

import time
import webbrowser

count = 0

print("This program started on "+time.ctime())

while (count < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=CGhz57AlmLw")
    count += 1
