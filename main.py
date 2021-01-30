#!/usr/bin/python3
# Password Generator with Lower and Upper Cases (string), numbers and symbol
import random 
import string 
import sys
import time
import datetime
import os
from os import path 

print("\n")
print("Welcome to my Random Password Generator!\n")

random = ''.join([random.choice(string.ascii_lowercase + 
string.ascii_uppercase + string.digits) for x in range(12)])    # 12 words long generated password

print("\n")

def pw():            
    print("***********************************************")
    print("** Your Generated Password is: ", random ,"**")
    print("***********************************************")
    print("\n")
    
def check_user():
    check = str(input("Do you want to keep this password? (y/n) : ")).lower().strip()
    try:
        if check == 'y':
            ask_user = input("For what usage is it needed? : ")
            print("Congratulations, your password has been saved in your .txt file")
            text_file = open("rpg.txt", "a+")
            n = text_file.write("\n""Generated Password is: "+ random + "\n"
                "Date: " + time.strftime("%d.%m.%Y | Time: %H:%M:%S") + "\n"
                "Account: " + ask_user + "\n")
            text_file.close()
            return True
        elif check == 'n':
            return False
        else:
            print('Please Enter (y) or (n)!')
            return check_user()
    except Exception as error:
        print('Please Enter (y) or (n)!')
        return check_user()


# def addToClipboard(text):
    # command = 'echo | set /p nul=' + text.strip() + '| clip'
    # os.system(command)



if __name__ == '__main__':
    pw()
    check_user()
    # addToClipboard(random)
