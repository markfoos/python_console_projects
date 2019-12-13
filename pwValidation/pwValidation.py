#password protection program, ran in console, proof of concept
#for backend python programming, Created by Mark Foos

import re
#main password function, returning True or False

def checkPassword(password):

    #put in regex variable search terms

    alphaUpper = "(?=.*[A-Z])"
    specialChar = "(?=.*[!,?,#,@,%])"
    digit = "(?=.*\d)"
    alphaLower = "(?=.*[a-z])"


    #check the password length
    if len(password) < 8:
        print("Password needs to be at least 8 characters long")
        print("POSITIVE FEEDBACK      Would you like to keep trying? (y or n)")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True
#test for at least 1 Uppercase letter
    elif not re.findall(alphaUpper, password):
        print("Need that Uppercase letter")
        print("POSITIVE FEEDBACK        Would you like to keep trying? (y or n)")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True
#check for at least 1 digit
    elif not re.findall(digit, password):
        print("Need at least 1 digit")
        print("POSITIVE FEEDBACK        Would you like to keep trying? (y or n)")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True
#check for at least 1 special character (!, ?, #, @, or %)
    elif not re.findall(specialChar, password):
        print("Need at least 1 special char (!, ?, #, @, %)")
        print("POSITIVE FEEDBACK      Would you like to keep trying? (y or n)")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True
#check for at least 1 lowercase letter
    elif not re.findall(alphaLower, password):
        print("Need a lowercase letter, even though it is not required in the assignment, I've added it to be thorough")
        print("POSITIVE FEEDBACK    Would you like to keep trying? (y or n)")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True
#return true if all these paramenters are met
    else:
        print("This password matches all parameters, POSITIVE FEEDBACK")
        print("Would you like to test more passwords? (y or n)\n")
        question = input()
        if str.lower(question) == 'y':
            return False
        else:
            return True


print("." * 100)
print("Welcome to Password Validator")
print("." * 100)
print("." * 100)
print("Hi Michael, this is some flair text to keep things interesting")
print("." * 100)
print("Password requirements are 1 upper, 1 lower, at least 8 characters and")
print("At least 1 special character (!, ?, #, @, or %))")
print("Also, your input will be stripped of all white space and <>, $, (), or *")
print("." * 100)

password_Valid = False
#main while loop to break with correct password
while not password_Valid:

    passwordRaw = input("Enter your mother truckin Password: \n")
    password = passwordRaw.strip(" <>$()*")
    password_Valid = checkPassword(password)
###  Regex parameters from Stack Overflow
#    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"






#pw_ReGex = re.compile(str(user_password))






#print(testSpecialChar)



#print(pw_ReGex)

#mo = pw_ReGex.search("0", "1", "2", "3")
#print(mo)

#moVarLower = pw_ReGex.search("abcdefghijklmnopqrstuvwxyz")
#print(moVarLower)

#moVarUpper = pw_ReGex.search("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#print(moVarUpper)
