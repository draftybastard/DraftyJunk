# Function has a single string parameter that it checks s is a single word starting with "pre"
#
# Check if word starts with "pre"
# Check if word .isalpha()
# if all checks pass: return True
# if any checks fail: return False
# Test
# get input using the directions: *enter a word that starts with "pre": *
# call pre_word() with the input string
# test if return value is False and print message explaining not a "pre" word
# else print message explaining is a valid "pre" word
# # [ ] create and test pre_word()


def pre_word(user_word):
    if user_word.isalpha():
        if user_word.lower()[0:3] == "pre":
            return True

        else:
            return False


def test():
    if pre_word(user_word):
        print("nailed it!")
    else:
        print("nah")


user_word = input("Like the usual, gimme a word")
test()


