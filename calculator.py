num1 =float(input("enter a number:"))
operator=input("enter operator(+,-,*,/):")
num2=float(input("enter second number:"))

if operator=="+":
    print("Result:",num1+num2)
elif operator=="-":
    print("Result:",num1-num2)
elif operator=="*":
    print("Result:",num1*num2)
elif operator=="/":
 if num2 ==0:
  print("error!division by zero is not allowed.")
 else:
    print("Result:",num1/num2)
else:
       print("invalid oprator!please use +,-,*,or/.")
