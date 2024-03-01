income = int(input("Enter your income: "))

sal_income = bool(input("Is this salary based income? T/F: "))
if sal_income:
    income -= 50000 

tax_sl= int(income/300000)
tax_amt = 0

if income > 700000: 
    if tax_sl == 0:
        tax_amt = 0
    elif tax_sl == 1:
        tax_amt =  income * .05
    elif tax_sl == 2:
        tax_amt = 15000 + ((income - 600000) * .1)
    elif tax_sl == 3:
        tax_amt = 45000 + ((income - 900000) * .15)
    elif tax_sl == 4:
        tax_amt = 150000 + ((income - 1200000) * .2)
    elif tax_sl >= 5:
        tax_amt = 240000 + ((income - 1500000) * .3)

    tax_amt += tax_amt *.04   #CESS 4%
    print("Tax amount value = ", tax_amt)
else:
    print("No taxation") 
