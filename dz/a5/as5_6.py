t=float(input("Temperature value in degree Celsius: "))

print("The %.2f degree Celsius is equal to:" %t,end=" ")
print("%.2f Fahrenheit" %(t*(9/5)+32),end='\n')
print("The %.2f degree Celsius is equal to:" %t,end=" ")
print("%.2f Kelvin" %(t+273.15),end='\n')