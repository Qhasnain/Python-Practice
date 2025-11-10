bigger=lambda a,b:"both are same " if a==b else(a if a>b else b) 

num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))

print("Biggest Number is :",bigger(num1,num2))