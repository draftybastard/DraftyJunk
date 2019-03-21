# incrementing in a while() loop
# Program: Shirt Count
# enter a sizes (S, M, L)
# tally the count of each size
# input "exit" when finished
# report out the purchase of each shirt size
#  [ ] Create the Shirt Count program, run tests
#
#
# CHALLENGE: Shirt Register (optional)
# Update the Shirt Count program to calculate cost
#
# use shirt cost (S = 6, M = 7, L = 8)
# to calculate and report the subtotal cost for each size
# to calculate and report the total cost of all shirts
# [ ] Create the Shirt Register program, run tests


def shirt_count():
    small = 0
    med = 0
    lrg = 0
    while True:
        user_input = input("Small, Medium, Large or Exit? \n\t")
        if user_input.lower() == "s":
            print("Adding Small")
            small += 1
            continue
        elif user_input.lower() == "m":
            print("Adding Medium")
            med += 1
            continue
        elif user_input.lower() == "l":
            print("Adding Large")
            lrg += 1
            continue
        elif user_input.lower() == "x":
            print("And....we out.")
            break
        else:
            print("Ehhh")
            continue
    print("There are {} Large, {} Medium, and {} Smalls".format(lrg, med, small))
    print()
    print("That's going to cost {}, {}, {}".format(lrg*8, med*6, small*5))


shirt_count()


