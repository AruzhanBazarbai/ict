n=float(input());
tip=n*0.18;
tax=n*0.15;
n=n+tip+tax;
# print(type(tip),type(tax),type(n));
print(f"grand total for the meal: {n:.2f}");
