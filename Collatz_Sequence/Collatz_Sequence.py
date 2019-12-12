#collatz sequence project
#created by Mark Foos
#original script inspired by Automate the Boring Stuff with Python
print("-" * 100)
print("Welcome to Collatz Sequence")
print("-" * 100)

print("\nEnter a Number\n")

#get a valid input from user
def number_input():
    number_entered = False
    while number_entered == False:
        try:
            varX = int(input())
            return varX
            number_entered == True
        except:
            print("\nEnter an integer")
            continue

#main function to run the collatz
def collatz(number):


    while not number == 1:
        if (number % 2) == 0:
            number = (number // 2)
            print(number)
            input("Press Enter")


        else:

            number = (number * 3 + 1)
            print(number)
            input("Press Enter")

#nested input function inside collatz function
collatz(number_input())
