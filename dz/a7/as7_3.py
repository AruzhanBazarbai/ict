weight=int(input("weight = "))
height=float(input("height = "))
bmi=round(weight/(height*height))
res=""
if bmi<18.5:
    res="underweight."
elif bmi>=18.5 and bmi<25:
    res="normal weight."
elif bmi>=25 and bmi<30:
    res="slightly overweight."
elif bmi>=30 and bmi<35:
    res="obese."
else:
    res="clinically obese."
print("Your BMI is "+str(bmi)+", you are "+res)