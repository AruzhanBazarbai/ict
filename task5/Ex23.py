import math
s,n=map(int,input().split())
a=n*(s*s/(4*math.tan(math.pi/n)))
print(f"area is: {a:.3f}")