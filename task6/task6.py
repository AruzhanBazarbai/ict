# Ex 1 -done
s=input()
s=s.lower();
res=""
for x in s:
    if x=='a' or x=='o' or x=='y' or x=='e' or x=='u' or x=='i':
        continue
    else:
        res+='.'+x
print(res)
# Ex 2 -done
s=input()
res=""
a=[]
for i in range (len(s)):
    if i%2==0:
        a.append(int(s[i]))
a=sorted(a)
for i  in range(len(a)):
    res+=str(a[i])
    if(i!=len(a)-1):
        res+='+'
print(res)
# Ex 3 -done
s=input()
x=s.upper()
s=s.replace(s[0],x[0])
print(s)
# Ex 4 - done
s=input()
cnt=1
x=s[0]
k=True
for i in range(1,len(s)):
    if x==s[i]:
        cnt+=1
    else:
        cnt=1
    
    if cnt>=7:
        k=False
        break
    x=s[i]

if k:
    print("NO")
else:
    print("YES")
# Ex 5-done
s=input()
s=sorted(s)
res=s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        res+=s[i]
if len(res)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
# Ex 6 - done
s=input()
cnt1=cnt2=0
for x in s:
    if ord(x)>=ord('A') and ord(x)<=ord('Z'):
        cnt1+=1
    else:
        cnt2+=1
if cnt1>cnt2:
    print(s.upper())
else:
    print(s.lower())
# Ex 7 - done
n=int(input())
s=str(input())
s=sorted(s.lower())
res=s[0]
cnt=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        res+=s[i]
for x in res:
    if (ord(x)>=ord('A') and ord(x)<=ord('Z')) or (ord(x)>=ord('a') and ord(x)<=ord('z')):
        cnt+=1
if cnt>=26:
    print("YES")
else:
    print("NO")
# Ex 8 - done
s=input()
x=input()
s=s[::-1]
if s==x:
    print("YES")
else:
    print("NO")
# Ex 9 - done
n=int(input())
s=input()
cntA=cntD=0
for x in s:
    if x=='A':
        cntA+=1
    else:
        cntD+=1
if cntA>cntD:
    print("Anton")
elif cntA<cntD:
    print("Danik")
else:
    print("Friendship")
# Ex 10 - done
s=input()
x=s
s=s.lower()
x=x.upper()
s=s.replace(s[0],x[0])
print(s)
# Ex 11 - done
n=int(input())
s=input()
cnt1=cnt0=0
for i in range(n):
    if s[i]=='z':
        cnt0+=1
    elif s[i]=='n':
        cnt1+=1
res=""
while cnt1>0:
    res+='1 '
    cnt1-=1
while cnt0>0:
    res+='0 '
    cnt0-=1

print(res)
# Ex 12 - done
n=int(input())
s=input()
cnt=0
for i in range(n-2):
    if s[i]=='x' and s[i+1]=='x' and s[i+2]=='x':
        cnt+=1
print(cnt)
