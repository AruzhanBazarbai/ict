s=input()
res=""
for i in range(len(s)):
    if s[i]==" ":
        if len(res)%2==0:
            print(res)
        res=""
    elif i==len(s)-1:
        res+=s[i]
        if len(res)%2==0:
            print(res)
        res=""
    else:
        res+=s[i]