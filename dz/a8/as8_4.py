from math import *
def prime_f(x):
    for i in range(2,int(sqrt(x)+1)):
        if x%i==0:
            return False
    return True


num1=int(input("Enter starting number: "))
num2=int(input("Enter ending number: "))
for i in range(num1,num2+1):
    pr=prime_f(i)
    if pr:
        print(i)
