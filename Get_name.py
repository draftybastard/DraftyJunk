# create variable, familar_name, and assign it an empty string ("")
# use while True:
# ask for user input for familar_name (common name friends/family use)
# keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# break loop and print a greeting using familar_name
# [ ] create Get Name program

while True:
    familiar_name = input("What's your daddy's name")
    if familiar_name.isalpha() and familiar_name.istitle():
        print("I'm sure your daddy was an excellent man, {} is a great name. ".format(familiar_name))
        break
    else:
        print("That ain't no name, son.")
