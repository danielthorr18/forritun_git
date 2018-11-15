Original_Amount = float(input("Input the cost of the item in $: "))
Remaining_debt = Original_Amount
month = 0
fully_paid = False
total_interest = 0
total_months = 0


if Original_Amount <= 1000:
    interest_rate = 0.015
else:
    interest_rate = 0.02

while fully_paid == False:
    monthlyInterest = Remaining_debt * interest_rate
    if Remaining_debt >= 50:
        totalMonthlypayment = 50
    else:
        totalMonthlypayment = Remaining_debt + monthlyInterest

    month += 1

    monthlyLoanpayment = totalMonthlypayment - monthlyInterest
    Remaining_debt -= monthlyLoanpayment

    total_interest += monthlyInterest
    total_months += 1

    print('Month:', (month), 'Payment:', round(totalMonthlypayment, 2), 'Interest paid: ', round(monthlyInterest, 2), 'Remaining debt: ', round(Remaining_debt, 2))

    if Remaining_debt ==0:
        fully_paid = True

print("number of months: ", (total_months))
print("total interest paid: ", round(total_interest, 2))
    

    






