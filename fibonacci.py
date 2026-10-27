
n=int(input("enter any number:"))
x,y=0,1
count=0
if n<=0:
    print("enter a postivive number.")
elif n==1:
    print("fibonacci sequence upto",n,":")
    print(x)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(x)
        z=x+y
        x=y
        y=z
        count=count+1