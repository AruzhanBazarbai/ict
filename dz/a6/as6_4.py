text=input("text: ")
word=input("word: ")
res=""
ok=False
for i in range(len(text)):
    if text[i]==" ":
        if word==res:
            ok=True
            break
        res=""
    elif i==len(text)-1:
        res+=text[i]    
        if word==res:
            ok=True
            break
        res=""
    else:
        res+=text[i]
if ok:
    print("True")
else:
    print("False")