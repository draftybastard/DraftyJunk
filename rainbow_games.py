# print the color matching the letter
# R = Red
# O = Orange
# Y = Yellow
# G = Green
# B = Blue
# I = Indigo
# V = Violet
# else print "no match"
# [ ] complete rainbow colors
#
#
#
# [ ] make the code above into a function rainbow_color() that has a string parameter,
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.


def rainbow_color(color_call):
    if color_call.upper() == "R":
        print("Red")
        return
    if color_call.upper() == "O":
        print("Orange")
        return
    if color_call.upper() == "Y":
        print("Yellow")
        return
    if color_call.upper() == "G":
        print("Green")
        return
    if color_call.upper() == "B":
        print("Blue")
        return
    if color_call.upper() == "I":
        print("Indigo")
        return
    if color_call.upper() == "V":
        print("Violette")
        return
    elif color_call.upper() != "R" or "O" or "Y" or "G" or "B" or "I" or "V":
        print("no.")
        return False


def age_20(input_age):
    input_age_string = "Your age, modified by 20 is {}".format(input_age)
    if input_age >=20:
        input_age -=20
        return input_age_string
    else:
        input_age += 20
        return input_age_string


def rain_or_age()

user_color = input("What's the first letter of your favorite color of the rainbow?")
user_age = input("Now, for some dumb reason, I need your age! ")
age_20(user_age)
rainbow_color(user_color)


#
# R = Red
# O = Orange
# Y = Yellow
# G = Green
# B = Blue
# I = Indigo
# V = Violet
# else print "no match"