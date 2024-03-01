import math
num=float(input("Enter a positive number: ")) 
tol=0.000001                                  
est=1.0                                       

while True:
    est=(est+ num/est)/2
    diff=abs(num - est ** 2)
    if diff <= tol:
        break

print("the program's resulting estimate value: ",est)
print("python estimate value: ", math.sqrt(num))
