# // # s="This is the lion in the cage"
# // # s=s.replace("the","")
# // # print(s)

# // n,s=input().split()
# // n=int(n)
# // for i in range(0,n):
# //     if ord(s[i]<ord('a') or ord(s[i])>ord('z'):
# //         s=s.replace()
age=int(input("Enter the age: "))
sx=input("Enter the sex: ")
ms=input("Enter the marital status: ")
if sx=="F":
    print("she will work only in urban areas")
elif sx=="M" and age>=20 and age<40:
    print("he may work in anywhere")
elif sx=="M" and age>=40 and age<60:
    print("he will work in urban areas only")
else:
    print("ERROR")

from math import *
def prime_f(x):
    for i in range(2,int(sqrt(x)+1)):
        if x%i==0:
            return False
    return True

start=int(input("start = "))
end=int(input("end = "))
print("Prime numbers between ",start," and ",end," are:")
for i in range(start,end+1):
    pr=prime_f(i)
    if pr:
        print(i)


