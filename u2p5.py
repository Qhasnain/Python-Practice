def is_prime(num):
    if num<=1:
        return False
    i=2
    while i<=num/2:
        if num%i==0:
            return False
        i+=1
    return True

limit=int(input("Enter YOur limit :"))

print("Prime numbers are :")
for n in range(2,limit+1):
    if is_prime(n):
       print(n,True)
    else:
        print(n,False)
    
    