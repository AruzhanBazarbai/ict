# Ex 6
n=float(input());
tip=n*0.18;
tax=n*0.15;
n=n+tip+tax;
# print(type(tip),type(tax),type(n));
print(f"grand total for the meal: {n:.2f}");
# Ex 9
m=int(input());
year=1;
balance=m;
while year<=3:
    balance+=balance*0.04;
    print(f"amount in the saving account after {year} year: {balance:.2f}");
    year+=1;
# Ex 11
g=int(input())
g1=3.78543
m1=1.6093
can=100/m1/g*g1
print(can)
# Ex 12
import math
t1,g1,t2,g2=map(int,input().split())
t1=math.radians(t1)
g1=math.radians(g1)
t2=math.radians(t2)
g2=math.radians(g2)
d=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(d)
# Ex 13
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
# Ex 19
d=int(input())
vf=2*9.8*d
print(vf)
#  Ex 23
import math
s,n=map(int,input().split())
a=n*(s*s/(4*math.tan(math.pi/n)))
print(f"area is: {a:.3f}")
#  EX 24
d,h,m,s=map(int,input().split())
seconds=d*86400+h*3600+m*60+s
print(seconds)
#  Ex 25
seconds=int(input())
d=seconds//86400
seconds%=86400
h=seconds//3600
seconds%=3600
m=seconds//60
seconds%=60
if(d<10):
    d1='0'+str(d)
elif(d>=10):
    d1=str(d)

if(h<10):
    h1='0'+str(h)
elif(h>=10):
    h1=str(h)

if(m<10):
    m1='0'+str(m)
elif(m>=10):
    m1=str(m)

if(seconds<10):
    s1='0'+str(seconds)
elif(seconds>=10):
    s1=str(seconds)
print(f"{d1}:{h1}:{m1}:{s1}")
#  Ex 27
h,w=map(int,input().split())
bmi=w/(h*h)
print(bmi)
#  Ex 28
t,v=map(int,input().split())
wci=13.12+0.6215*t-11.37*(v**0.16)+0.3965*t*(v**0.16)
if t<=10 and v>4.8: 
    print(wci)
