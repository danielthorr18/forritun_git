def getShares():
    while True:
        try:
            shares = int(input("Enter number of shares: "))
            return shares
        except ValueError:
            print("Invalid number!")


def getPrice():
    while True:
        price = input("Enter price (dollars, numerator, denominator): ")
        splitPrice = ''.join(price.split())
        try:
            splitPrice = int(splitPrice)
            return price
        except ValueError:
            print("Invalid price!")



def convertPrice(price):
    dollars, numerator, denominator = price.split()
    numerator, denominator = int(numerator), int(denominator)
    fraction = str(numerator / denominator).replace('0.', '')
    convertedPrice = float(dollars + '.' + fraction)
    return convertedPrice

def calculateMarketPrice(convert, shares):
    convertedPrice = float(shares * convert)
    return convertedPrice

def finish():
    if input("Continue: ") == 'y'.lower():
        return False
    else:
        return True


def printMarketValue(shares, price, marketprice):
    print('{} shares with market price {} have value ${:.2f}'.format(shares, price, marketprice))

finished = False
while finished == False:
    shares = getShares()
    price = getPrice()
    convert = convertPrice(price)
    marketprice = calculateMarketPrice(convert, shares)
    printMarketValue(shares, price, marketprice)
    finished = finish()
    
    print(price)
    print(convert)
    print(marketprice)



