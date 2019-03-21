# Pet Conversation
# ask the user for a sentence about a pet and then reply
#
# get user input in variable: about_pet
# using a series of if statements respond with appropriate conversation
# check if "dog" is in the string about_pet (sample reply "Ah, a dog")
# check if "cat" is in the string about_pet
# check if 1 or more animal is in string about_pet
# no need for else's
# finish with thanking for the story
#  [ ] complete pet conversation

def check_pet(user_input):
    if "dog".lower() in user_input:
        print("Oh, you've got a puppy!")
    if "cat".lower() in user_input:
        print("Fuck Cats")
    if "dog".lower() and "cat".lower() in user_input:
        print ("that's too many")
    print("I heard you tell me about " + user_input + "And I thank you for it.")


user_story = input("Tell me about your first pet, make sure to tell me what type! ".lower())
check_pet(user_story)
