t,v=map(int,input().split())
wci=13.12+0.6215*t-11.37*(v**0.16)+0.3965*t*(v**0.16)
if t<=10 and v>4.8: 
    print(wci)
