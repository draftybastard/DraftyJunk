# Program: adding_report() function
# This program calls the adding_report() function which repeatedly takes positive integer input until the user
# quits and then sums the integers and prints a "report".
# The adding_report() function has 1 string parameter which indicates the type of report:
#
# "A" used as the argument to adding_report() results in printing of all of the input integers and the total
# "T" used as the argument results in printing only the total
# BIG PICTURE: call function with A or T,

# This program requires the use of while loop, if, elif, else, if, else (nested), casting of type, between strings and
# numbers. The program should only use code syntax covered in modules 1 - 4. The program must result in print output
# using the numeric input, similar to that shown in the samples displaying "Items" and "Total".

#  HEY YOU, YEAH, GREGG, use a for i in list in here somewhere...to list the numbers being talleyed
# i.e for every number in talley: print number


def adding_machine(output_type):
    number = ""  # our variable for user input number
    talley = []  # Using a list to utilize the .add function, will explore using string methods once running
    while output_type.lower == 'a':  # setting the more info heavy output as default
        number = input("Input any whole number, |q| to quit")
        if number.isnumeric():
            talley.append(number)
        elif number.isalnum():
            print("Not so fast, bub")
            continue
        elif number.isalnum():
            if number.lower == 'a':
                return
            else:
                print("nope, only one letter allowed, and that ain't it.")
                return



