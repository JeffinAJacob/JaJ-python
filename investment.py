invt=float(input("Enter the investment amount: "))  #investment
yrs=int(input("Enter the number of years: "))       #years
rate=float(input("Enter the rate as a %: ")) / 100  #rate
stbal=invt #starting balance
totalin=0  #total interest
print("Year\tStarting balance\tInterest\tEnding balance")
for yrs in range(1,yrs+1):
    inrt=stbal*rate
    enbal=stbal+inrt  #end balance
    print("%4d  %18.2f\t%10.2f\t%16.2f" % \
          (yrs, stbal, inrt, enbal))
    stbal=enbal
    totalin=totalin+inrt
    
print("\nEnding balance: %0.2f " % enbal)
print("\nTotal interest earned: %0.2f " % totalin)
