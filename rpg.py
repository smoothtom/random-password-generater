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

random = ''.join([random.choice(string.ascii_lowercase + 
string.ascii_uppercase + string.digits) for x in range(12)])    # 12 words long generated password

print("\n")

def query():            
    print("*********************************************")
    print("Your Generated Password is: ", random)
    print("*********************************************")
    print("\n")

query()

ask_first = input("Do You want to keep this password? (yes or no) : ")
if ask_first == "yes":
    ask_user = input("For what usage is it needed? : ")
    print("Congratulations, your password has been saved in your .txt file")
else:
    sys.exit(0)

text_file = open("rpg.txt", "a+")
n = text_file.write("Generated Password is: "+ random + "\n"
        "Time: " + time.strftime("%d.%m.%Y um %H:%M:%S Uhr") + "\n"
        "Usage: " + ask_user + "\n")
text_file.close()

