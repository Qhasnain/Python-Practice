keys = ['name', 'age', 'city']
values = ['Ali', 22, 'Mumbai']

result=dict(zip(keys,values))
print(result)
#with lambda
#result=dict(map(lambda a:(a[0],a[1]),zip(keys,values)))