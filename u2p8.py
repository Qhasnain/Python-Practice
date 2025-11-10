#Positional Argument :
def positional(a,b):
        print(a+b)

a=int(input("Enter Number 1 :"))
b=int(input("Enter Number 2 :"))

positional(a,b)

#Keyword Argument :
def key(name ,a,b):
    print(a+b,name)

key(b=12,a=43,name="Hasnain")
    
#Default Argument :
def de(a,b,c=0):
    print(a+b,c)
a=int(input("Enter Number 1 :"))
b=int(input("Enter Number 2 :"))
de(a,b)

#Variable Length :
def var(*abc):
    print(abc)
var(2,"Hasnain")