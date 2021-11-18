m=int(input());
year=1;
balance=m;
while year<=3:
    balance+=balance*0.04;
    print(f"amount in the saving account after {year} year: {balance:.2f}");
    year+=1;