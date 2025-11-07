list1=[1,3,5,3,2]
list2=[2,1,4,3,5]
common=[]
for x in list1:
    if x in list2:
        common.append(x)

non_common=[]

for x in list1+list2:
    if(x not in list1)or (x not in list2):
        non_common.append(x)
print("List 1 :",list1)
print("List 2 :",list2)
print("Common value :",common)
print("NonCommon value :",non_common)