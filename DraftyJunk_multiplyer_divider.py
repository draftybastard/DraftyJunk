# check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)
# - if guess is not an alpha character print invalid and return False - test and print if guess is "high" or "low"
# and return False - test and print if guess is "correct" and return True


def check_guess(letter, guess):

    if letter.isalpha() == False:
        return False
    elif letter.lower() > guess:
        print ("{} is too low ".format(guess))
        return False
    elif letter.lower() < guess:
        print ("{} is too high ".format(guess))
        return False
    elif letter.lower() == guess:
        print("GET OUT OF MY HEAD! ")
        return True
    else:
        print("I don't know how you did what you did, but it ain't right. ")


letter = "d"
print("We're gonna play a real stupid game...")
print("We're gonna guess some fucking letters, bro!")
guess_out = input("What's your letter?")
print(check_guess(letter, guess_out))

