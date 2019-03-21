# Letter Guess
# create letter_guess() function that gives user 3 guesses
#
# takes a letter character argument for the answer letter
# gets user input for letter guess
# calls check_guess() with answer and guess
# End letter_guess if
# check_guess() equals True, return True
# or after 3 failed attempts, return False
# [ ] create letter_guess() function, call the function to test

def letter_guess(guess, answer, count):
    if count <= 3:
        count + 1
        if guess.lower() >= answer.lower():
            print("Guess is higher than answer")
            count + 1
        elif guess.lower() <= answer.lower():
            print("Guess is lower than answer")
            count + 1
        elif guess.lower() == answer.lower():
            print("Winner!")
            count + 3
        else:
            print("Not sure what you did, but stop it")
            count + 3


user_guess = input("What's your letter, lets see if it matches mine")
user_answer = "r"
user_count = 0
letter_guess(user_guess, user_answer, user_count)
