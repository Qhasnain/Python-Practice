players = {'Virat': 85, 'Rohit': 42, 'Rahul': 56, 'Dhoni': 90}
ab50=dict(filter(lambda a:a[1]>50 , players.items()))

print("Players with above 50 runs :")

for name,score in ab50.items():
    print(f"{name} : {score}")