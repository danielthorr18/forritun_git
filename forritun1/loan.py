loan = float(input("Input the cost of the item in $: "))
month = 1
totalTax = 0
if loan > 1000:
    while loan > 0:
        if loan <= 50: 
            vextir = loan*0.02
            pay = loan + vextir
            loan = loan - loan
            print("Month:", month, "Payment:", round(pay,2), "Interest paid:", round(vextir,2), "Remaining debt:", round(loan,2))
            totalTax += vextir
        elif loan > 50:
            vextir = loan*0.02
            pay = 50.0
            loan = loan - pay + vextir
            print("Month:", month, "Payment:", round(pay,2), "Interest paid:", round(vextir,2), "Remaining debt:", round(loan,2))
            month += 1
            totalTax += vextir
else: 
    while loan > 0:
        if loan <= 50: 
            vextir = loan*0.015
            pay = loan + vextir
            loan = loan - loan
            print("Month:", month, "Payment:", round(pay,2), "Interest paid:", round(vextir,2), "Remaining debt:", round(loan,2))
            totalTax += vextir
        elif loan > 50:
            vextir = loan*0.015
            pay = 50.0
            loan = loan - pay + vextir
            print("Month:", month, "Payment:", round(pay,2), "Interest paid:", round(vextir,2), "Remaining debt:", round(loan,2))
            month += 1
            totalTax += vextir

print("Number of months:", month)
print("Total interest paid:", round(totalTax,2))
        
        
        
        
        
        
        