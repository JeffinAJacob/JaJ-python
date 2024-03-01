
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0


grossIncome = float(input("Enter the gross income: "))
nunDependents = int(input("Enter the number of dependents: "))


taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * nunDependents
incomeTax = taxableIncome * TAX_RATE


print("The income tax is $"+ str(incomeTax))
