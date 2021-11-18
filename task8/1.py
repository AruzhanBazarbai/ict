n=int(input("Enter rows number: "))
while n:
    temp = n
    while(temp):
        print(temp,end=" ")
        temp-=1
    print(end='\n')
    n-=1