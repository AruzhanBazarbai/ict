# Ex1 - done

pizza_S=15
pizza_M=20
pizza_L=25
pepp_S=2
pepp_M_L=3
cheese=1
bill=0

while True:
    s=input()
    if s=="":
        break
    s1,s2,s3=s.split(" ")
    res1=s1
    res2=s3[1]

    if res1=="size":
        if res2=="L":
            bill+=pizza_L
        elif res2=="M":
            bill+=pizza_M
        elif res2=="S":
            bill+=pizza_S
    elif res1=="add_pepperoni":
        if res2=="Y":
            if bill==25 or bill==20:
                bill+=pepp_M_L
            else:
                bill+=pepp_S
    elif res1=="extra_cheese ":
        if res2=="Y":
            bill+=cheese

print("Your final bill is: $"+str(bill)+".")

# Ex2 - done

year=int(input())
if year%4==0 and year%100==0 and year%400==0:
    print("Leap year.")
elif year%4==0 and year%100!=0:
    print("Leap year.")
else:
    print("Not leap year.")

# Ex3 - done

weight=int(input())
height=float(input())
bmi=round(weight/(height*height))
res=""
if bmi<18.5:
    res="underweight."
elif bmi>=18.5 and bmi<25:
    res="normal weight."
elif bmi>=25 and bmi<30:
    res="slightly overweight."
elif bmi>=30 and bmi<35:
    res="obese."
else:
    res="clinically obese."
print("Your BMI is "+str(bmi)+", you are "+res)

# Ex4 - done

salary=int(input())
year=int(input())
bonus=0
if year>5:
    bonus=salary*0.05
print(bonus)

# Ex5 - done

length,breadth=map(int,input().split())
if length==breadth:
    print("Square")
else:
    print("Not square")

# Ex6 - done

q=int(input())
cost=q*1000
if cost>1000:
    cost=cost+cost*0.1
print(int(cost))

# Ex7 - done

mark=int(input())
if mark<25:
    print("F")
elif mark>=25 and mark<45:
    print("E")
elif mark>=45 and mark<50:
    print("D")
elif mark>=50 and mark<60:
    print("C")
elif mark>=60 and mark<80:
    print("B")
else:
    print("A")

# Ex8 - done

a,b,c=map(int,input().split())
print(max(a,max(b,c)),min(a,min(b,c)))

# Ex9 - done

held=int(input("Number of classes held: "))
attended=int(input("Number of classes attended: "))
p=attended/(held/100)

if p>=75:
    print("Percentage of class attended is: "+str(p)+",so student is allowed to sit in exam.")
else:
    print("Percentage of class attended is: "+str(p)+",so student isn't allowed to sit in exam.")

# Ex10 - done

n=int(input())
last=n%10
if last%3==0:
    print("Yes,last digit of "+str(n)+" is divisible by 3")
else:
    print("No,last digit of "+str(n)+" isn't divisible by 3")

