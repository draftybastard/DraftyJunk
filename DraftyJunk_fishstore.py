def shirt_store (size, cost):
    if size.lower() == "xxl":
        cost = 9.00
    elif size.lower() == "xl":
        cost = 7.00
    elif size.lower() == "l":
        cost = 6.00
    else:
        cost = 5.50
    print("If you're gonna buy a {} shirt, it'll cost ya {}".format(size, cost))


size = input("XXL, XL, L, M, S, Junkie")
cost = 0
shirt_store(size, cost)

