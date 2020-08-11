a = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the elements: "))
    a.append(x)
print("The array is:")
print(a)
num = int(input("Enter element you want to insert: "))
pos = int(input("Enter the position: "))
for i in range(n-1, pos-1):
    a[i+1] = a[i]
a[pos-1] = num
n += 1
print(a)