# make a program which allows the user to pick between sandwiches, return their order and value
# sub divide cheeze selection and allow a meat and vegan option

def sandwich_shoppe(user_option): # This will convert the user input into something our program understands
    if user_option.isalpha() == False:
        print("NO!")
        return False
    else:
        if user_option.lower() == "c":  # cheese logic
            cheese_type = input("(C)heddar, (A)merican, or (S)wiss? ")
            if cheese_type.lower() == "c":
                output = "Cheddar Cheese coming up!"
            elif cheese_type.lower() == "a":
                output = "American Classic coming up!"
            elif cheese_type.lower() == "s":
                output = "The Exotic Swiss!"
            else:
                output = "Umm...not sure what went wrong..."
            return output

        if user_option.lower() == "m":  # meat logic
            meat_type = input("(H)am, (B)eef, or (T)urkey? ")
            if meat_type.lower() == "h":
                output = "HHHHHHAAAAAMMMMMY Samy!"
                return output
            elif meat_type.lower() == "b":
                output = "Where's the beef?  In your hot little hands!"
                return output
            elif meat_type.lower() == "t":
                output = "Gobble Gobble, motherfuckers"
                return output
            else:
                output = "Yeah, no"
                return output
        if user_option.lower() == "v":  # logical logic
            output = "Soylent Green is peop...wait, vegan,coming up."
            return output


new_order = input("You going (m)eat, (c)heese, or (v)egan")
new_order.lower()
print(sandwich_shoppe(new_order))




# (C)heese:
#     (C)heddar
#     (A)merican
#     (S)wiss
# (M)eat:
#     (H)am
#     (B)eef
#     (T)urkey
# (V)egan:
#     (V)egan