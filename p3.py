data=bytearray([10,20,30,40,50])
print(type(data))
print("Orignal array :")
for value in data:
    print(value,end=" ")
    
for i in range(len(data)):
    data[i]=data[i]+5
    
print("\nModified array :")

for value in data:
    print(value,end=" ")
    
index=int(input("\nEnter value of index (0-4) :"))
print("\nValue at index ",index,"is:",data[index])
    