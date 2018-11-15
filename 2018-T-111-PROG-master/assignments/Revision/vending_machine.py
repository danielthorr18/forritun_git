CANDY_PRICE = 150
COIN_ERROR = -1


def display_menu(inserted):
    print("A packet of candy costs $ {:.2f}".format(CANDY_PRICE / 100), end="")
    print(". You have inserted $ {:.2f}.".format(inserted / 100))

    print("Please insert coins:" )
    print("\tn - Nickel")
    print("\td - Dime")
    print("\tq - Quarter")
    print("\tD - Dollar")


def accept_money():
    inserted = 0

    while inserted < CANDY_PRICE:
        display_menu(inserted)
        coin = input()

        cents = coin_to_cents(coin)
        if cents != COIN_ERROR:
            inserted += cents
        else:
            print("'{}' is not a valid coin.".format(coin))

    return inserted


def coin_to_cents(coin):
    if coin == 'n':
        return 5
    if coin == 'd':
        return 10
    if coin == 'q':
        return 25
    if coin =='D':
        return 100
    return COIN_ERROR


def compute_change(total_paid):
    return total_paid - CANDY_PRICE


def main():

    moneyEntered = accept_money()
    change = compute_change(moneyEntered)

    print("Enjoy your candies. Your change is $ {:.2f}. Please visit again.".format(change / 100))


main()