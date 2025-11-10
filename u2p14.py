from functools import reduce

tup=(10,20,30,40,50)
print("Maximum :",max(tup))
print("Minimum :",min(tup))

res=reduce(lambda a,b:a+b,tup)
avg=res/len(tup)
print("Sum of Tuple :",res)
print("Average of Tuple :",avg)