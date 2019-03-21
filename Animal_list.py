# Use while to get the user input, animal_name, of 4 animals
# use a counter, num_animals, in the while loop condition
# append the names to a string variable, all_animals
# User can exit early by typing "exit" (check if animal_name is "exit" and break)
# when the loop finishes, print the names of all_animals
# -bonus: print "no animals" if animal_name is empty after exiting the loop
#
# Tip: Think about Sequence and variables that need to be initialized before the while loop
#
# [ ] Create the Animal Names program, run tests


animal_list = []
counter = 3
animal = ""
while counter >= 0:
    animal = input("Gimme an animal name,eh? 'x' to exit, please")
    if animal == "x":
        break
    animal_list.append(animal)
    counter -= 1
    if len(animal_list) == 0:
        print("What?  There's nothing in the zoo! ")
print(animal_list)

