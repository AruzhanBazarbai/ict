n=int(input("Enter number: "))
sum=0
temp=n
while temp:
    sum+=temp
    temp-=1
print("Sum of first",n,"numbers is:",sum)
print("Average of",n,"numbers is:",sum/n)