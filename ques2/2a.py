list = []

n = int(input("Enter size:"))

for i in range(0,n):
    item = int(input("Enter a value"))
    list.append(item)

print(list)

if list.count(19)==2 or list.count(5)>=3:
    print("true")
else:
    print("false")