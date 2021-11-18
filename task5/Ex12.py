import math
t1,g1,t2,g2=map(int,input().split())
t1=math.radians(t1)
g1=math.radians(g1)
t2=math.radians(t2)
g2=math.radians(g2)
d=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(d)