n=int(input())
last=n%10
if last%3==0:
    print("Yes,last digit of "+str(n)+" is divisible by 3")
else:
    print("No,last digit of "+str(n)+" isn't divisible by 3")