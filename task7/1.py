q=int(input())
cost=q*1000
if cost>1000:
    cost=cost+cost*0.1
print(int(cost))