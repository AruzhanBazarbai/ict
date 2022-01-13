a=int(input())
i=1
while i<4:
    a*=1.04
    if i==1:
        print("After",i,"year: $%.2f" %a)
    elif i>1:
        print("After",i,"years: $%.2f" %a)
    i+=1