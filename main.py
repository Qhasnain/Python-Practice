import employe

name=input("Enter Name :")
basic=float(input("Enter Salary : "))

da=employe.DA(basic)
hra=employe.HRA(basic)
pf=employe.PF(basic)

gross=basic+da+hra
itax=employe.ITAX(gross)
net=gross-(pf+itax)

print(f"Employee Name :{name}")
print(f"Basic Salary  :{basic}")
print(f"DA(10%) :{da}")
print(f"HRA(15%) :{hra}")
print(f"PF(12%) :{pf}")
print(f"ITAX(8%) :{itax}")
print(f"Gross Salary :{gross}")
print(f"Net Salary : :{net}")