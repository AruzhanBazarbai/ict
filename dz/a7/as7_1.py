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