held=int(input("Number of classes held: "))
attended=int(input("Number of classes attended: "))
p=round(attended/(held/100))

if p>=75:
    print("Percentage of class attended is: "+str(p)+"%, so student is allowed to sit in exam.")
else:
    print("Percentage of class attended is: "+str(p)+"%, so student isn't allowed to sit in exam.")