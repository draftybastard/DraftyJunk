def age_20(input_age, adjust=20):
    if input_age <= 20:
        return input_age + adjust
    if input_age > 20:
        return input_age - adjust
    if input_age.isnumeric() !=True:
        pass
    else:
        return "Not sure what happened, but it ain't good.  What the heck is {}, anyways? ".format(input_age)


user_input = int(input("What's your age?"))
print("Your age is {} after adjustment".format(age_20(user_input, adjust=20)))


