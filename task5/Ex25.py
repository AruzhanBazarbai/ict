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