numbers=list(map(int,input().split()))
for x in numbers:
    if x>300:
        break
    if x>120:
        continue
    if x%3==0:
        print(x)