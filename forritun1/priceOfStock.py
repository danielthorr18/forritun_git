def clean_up(): #clean_up tekur strenginn price og aðskilur hann og setur gildin inn í breytur.
    while True:
        try:
            price = input("Enter price (dollars, numerator, denominator): ")
            splitter = price.split(" ")
            dollars = int(splitter[0])
            numerator = int(splitter[1])
            denominator = int(splitter[2])
            return dollars, numerator, denominator
        except Exception:
            print("Invalid price!")
def do_math(dollars, numerator, denominator): #do_math er fall sem sér um stærðfræðina.
    while True:
            fraction = float(numerator/denominator)
            samtals = num_shares * (dollars + fraction)
            return samtals

while True:
    try:
        num_shares = int(input("Enter number of shares: "))
        dollars, numerator, denominator = clean_up()
        samtals = do_math(dollars, numerator, denominator)

        print("{} shares with market price {} {}/{} have value ${:.2f}".format(num_shares, dollars, numerator, denominator, samtals))

        afram = input("Continue: ")
        if afram in "yY":
            continue
        elif afram in "nN":
            break

    except Exception:
        print("Invalid number!")