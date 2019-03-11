def fishstore(fish, price):
    return "The {} costs {}".format(fish.title(), price)


fish = input("What's for dinner?")
price = input("What'd that cost?")
print(fishstore(fish, price))


