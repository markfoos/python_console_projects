#to_do_list console program, developed by Mark Foos
import time
#identify list variables
numVar = []
to_do_list = []
list_ready = False

#intro
print("Welcome to the TO DO LIST program. \nEnter things to do when promted.")
print("Enter 'done' as a task when finished.")





#main loop function, creating two lists
while list_ready == False:
    listVar = str(input("Enter a List Item -- \ninput 'done' if finished\n"))
    
    if listVar.lower() == "done":
        list_ready = True
    else:
        print("Ok, adding \"" + str(listVar) + "\" to your list.")
        time.sleep(.300)
        to_do_list.append(listVar)
        numVar.append(len(numVar))

#make numVar list start at 1
for i in numVar:
    numVar[i] = int(i) + 1


#main print function
print("Here is your To Do List in Sequencial Order:")


#dictionary the two lists to print easier
dictionary = dict(zip(numVar, to_do_list))

print("-" * 99)
print("LIST NUMBER - LIST ITEM")
print("-" * 99)

for x in dictionary.items():
    print(x[0], "\t    ||\t", x[1])
    print("-" * 99)
