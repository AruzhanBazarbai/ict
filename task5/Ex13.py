# 100 cents=1 dollar
# 1 penny=1 cent
# 1 nickel=5 cents
# 1 dime=10 cents
# 1 quarter= 25 cents
# loonie= 1 dollar
# toonie= 2 dollar
cents=int(input("Enter amount of cents: "))
p=n=d=q=l=t=0
while cents>0:
    if  cents>=200:
        cents-=200
        t+=1
    elif cents>=100 and cents<200:
        cents-=100
        l+=1
    elif cents<100 and cents>=25:
        cents-=25
        q+=1
    elif cents<25 and cents>=10:
        cents-=10
        d+=1
    elif cents<10 and cents>=5:
        cents-=5
        n+=1
    elif cents>0 and cents<5:
        cents-=1
        p+=1
if t>0 :
    print(t," toonie")
if l>0 :
    print(l," loonie")
if q>0 :
    print(q," quarter")
if d>0 :
    print(d," dime")
if n>0 :
    print(n," nickel")
if p>0 :
    print(p," penny")
