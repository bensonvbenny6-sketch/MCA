n=int(input("enter any number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(n,"*",i,"=",fact)
print("factorial of",n,"is",fact)