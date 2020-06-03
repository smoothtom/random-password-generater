#!/usr/bin/python3
"""Password Generator with Lower and Upper Cases (string), numbers and symbols"""
import random 
import string 
import sys
import time
import datetime
import os
from os import path 

print("Welcome to my Random Password Generator!\n")

first_input = "s"   # s is the key 
"""x = input("First we have to check if you have the right file in your directory, please enter (s) to continue: ")"""

count = 0   # starts at 0 and goes to 3 

while count < 3:
    x = input("First we have to check if you have the right file in your directory, please enter (s) to continue: ")

    if x == first_input:
        break
    else:
        print("Please enter again: ")
        count +=1

random = ''.join([random.choice(string.ascii_lowercase + 
string.ascii_uppercase + string.digits) for x in range(12)])    # 12 words long generated password
print("\n")
def query():            
    print("*********************************************")
    print("Your Generated Password is: ", random)
    print("*********************************************")
    print("\n")

query() # execute the function above 

text_file = open("rpg.txt", "a+")
n = text_file.write("Generated Password is: "+ random +
        " " + "Time: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr" + "\n"))
text_file.close()

"""while True:
    if get_it == New:
       query()
       break
    else:
        sys.exit(0)"""
