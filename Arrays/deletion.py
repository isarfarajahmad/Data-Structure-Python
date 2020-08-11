a = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the elements: "))
    a.append(x)
print("The array is:")
print(a)
pos = int(input("Enter position you want to delete: "))
if pos <= 0 or pos > n:
    print("Invalid position !!!")
else:
    for i in range(pos-1, n-1):
        a[i] = a[i+1]
    a.pop()
    print("Now the array is:")
    print(a)