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


def adding_machine(report='t'):  # T prints only total, A prints all numbers, followed by total
    number = ""
    talley = 0
    while report.lower() == 't':
        number = input("Input an integer or \"q\" to quit")
        if number.isnumeric():
            talley += int(number)
        elif number.isalpha():
            if number.lower() == "q":  # Put print logic in here once the skeleton is done
                print(talley)
            else:
                print(number)


user_option = input("Are we looking for a full receipt or just the total? [1] Full Tally, [2] Total only \n")  #Make
#  This into a fucking loop!  We're gonna loop the world boyee!
if user_option == "1":
    adding_machine('a')
else:
    adding_machine('t')

