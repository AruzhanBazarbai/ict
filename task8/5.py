n=int(input("Enter number of terms: "))
a=0
b=1
while n:
    print(a,end=" ")
    c=b+a
    a=b
    b=c
    n-=1