# define function multiply(), and within the function:
# gets user input() of 2 strings made of whole numbers
#
# cast the input to int()
#
# multiply the integers and return the equation with result as a str()
#
# return example
# 9 * 13 = 117
#  [ ] create and test multiply() function


def calc(int1, int2, trigger):
    if trigger == "*":
        result = int1 * int2
    elif trigger == "/":
        result = int1 / int2
    else:
        result = "Special kinda dumb, eh?"
    return result


numb1 = int(input("What's the first number? "))
numb2 = int(input("What's the second number? "))
button = input("* or / ? ")
ans = calc(numb1, numb2, button)
print("{} {} {} = {}".format(numb1, button, numb2, ans))

