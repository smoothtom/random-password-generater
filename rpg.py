#!/usr/bin/python3
"""Password Generator with Lower and Upper Cases (string), numbers and symbols"""
import random 
import string 
import sys
import time
import datetime
import os 
print("Welcome to my Random Password Generator!\n")

random = ''.join([random.choice(string.ascii_lowercase + 
string.ascii_uppercase + string.digits) for x in range(8)])

def query():          
    print("*********************************************")
    print("Your Generated Password is: ", random)
    print("*********************************************")
    print("\n")

query()

text_file = open("rpg.txt", "a+")
n = text_file.write("Generated Password is: "+ random + " " + "Time: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr" + "\n"))
text_file.close()

"""while True:
    if get_it == New:
       query()
       break
    else:
        sys.exit(0)"""
