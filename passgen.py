import secrets 
from random import randint
import pyperclip

def getInput(question, validAns):
    userinput = input(question)
    while userinput.lower() not in validAns:
        userinput = input(question)
    return (userinput == 'y')
    
def getLength():
    try:
        length = int(input("Enter length of password (at least 8 characters):"))
        while (length < 8):
            print("Length must be at least 8 characters. Try again.")
            length = int(input("Enter length of password:"))
        return length  
    except ValueError:
        print("Invalid input. Try again")

def getLower():
    question = "Do you want to include lower case letters? (y/n)"
    return getInput(question, ['y', 'n'])

def getUpper():
    question = "Do you want to include upper case letters? (y/n)"
    return getInput(question, ['y', 'n'])

def getDigits():
    question = "Do you want to include digits? (y/n)"
    return getInput(question, ['y', 'n'])

def getSpChar():
    question = "Do you want to include special characters? (y/n)"
    return getInput(question, ['y','n'])

special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", ',', '.', '/', '<', '>', '?']

def conditions (password):
    countu = 0
    countl = 0
    counts = 0
    for char in password:
        if char in special:
            counts += 1
        if ord(char) <= 90 and ord(char) >= 65:
            countu += 1
        if ord(char) <= 122 and ord(char) >= 97:
            countl += 1
    return (countl > 0 and countu > 0 and counts > 0)

length = getLength()
lower = getLower()
upper = getUpper()
digits = getDigits()
spChar = getSpChar()

while True:
    password = ""
    for i in range (length):
        key = secrets.randbelow(4)
        if (key == 0 and lower):
            password += (chr(ord('a') + secrets.randbelow(26)))
        elif (key == 1 and upper):
            password += (chr(ord('A') + secrets.randbelow(26)))
        elif (key == 2 and digits):
            password += (str(randint(0,9)))
        else:
            if spChar:
                password += (secrets.choice(special))
    if(conditions(password)):
        break

print("Your randomly generated password is: " + password)

copy = input("Would you like to copy to clipboard? (y/n)")
while (copy.lower() != 'y' and copy.lower() != 'n'):
    copy = input("Would you like to copy to clipboard? (y/n)")

if (copy.lower() == 'y'):
    pyperclip.copy(password)


