num1=float(input("Enter Number 1 :"))
num2=float(input("Enter Number 2 :"))

print("location of num 1 ",id(num1))
print("location of num 2 ",id(num2))

if num1==num2:
    print("Both are same ")
else:
    print("Both are not same ")
