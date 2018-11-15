n = int(input("Enter the length of the sequence: "))

num1 = 0
num2 = 0
num3 = 0
sum_of_nums = 0

for number in range(1, n + 1): #range er frá 1 og að tölunni sem stimpluð er inn
    if number == 1: # ef talan er 1 þá prentast talan
        print(number)
        num1 = 1
    elif number == 2: #ef talan er 2 þá prentast talan
        print(number)
        num2 = 2
    elif number == 3: #ef talan er 3 þá prentast talan
        print(number)
        num3 = 3
    else: #ef talan er hvorki 1, 2 né 3 þá tekur við reikningur
        sum_of_nums = num1 + num2 + num3 #talan sem sleginn er inn er summa þriggja talna sem á undan henni koma
        num1 = num2 #loopan heldur svo áfram með því að fyrsta talan fær gildi annarar tölunnar
        num2 = num3 #önnur talan tekur gildi þriðju tölunnar
        num3 = sum_of_nums#þriðja talan fær gildi summu talnanna þriggja
        print(sum_of_nums)