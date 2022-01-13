s=input()
res=""
cnt_len=0
for i in range(len(s)):
    if s[i]==" ":
        cnt_len+=len(res)
        res=""
    elif i==len(s)-1:
        res+=s[i]    
        cnt_len+=len(res)
        res=""
    else:
        res+=s[i]
print(cnt_len)