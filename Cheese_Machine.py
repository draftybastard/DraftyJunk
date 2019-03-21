# Program: Cheese Order
# set values for maximum and minimum order variables
# set value for price variable
# get order_amount input and cast to a number
# check order_amount and give message checking against
# over maximum
# under minimum
# else within maximum and minimum give message with calculated price
# Sample input and output:
#
# Enter cheese order weight (numeric value): 113
# 113.0 is more than currently available stock
# Enter cheese order weight (numeric value): .15
# 0.15 is below minimum order amount
# Enter cheese order weight (numeric value): 2
# 2.0 costs $15.98
# # [ ] create, call and test
# # then PASTE THIS CODE into edX


def cheese_machine(amount_chz):
    if amount_chz <= min_order:
        return print("{} does not reach our minimum order.".format(str(amount_chz)))
    if amount_chz >= max_order:
        return print("{} is more than we have on stock, our apologies".format(str(amount_chz)))
    else:
        cost = amount_chz * chz_value
        return print("{} will be the total for {} grams of premium UK Cheese".format(str(cost), str(amount_chz)))


min_order = 1
max_order = 100
chz_value = 2.5
weight = int(input("How many grams of cheese, today?"))
cheese_machine(weight)
