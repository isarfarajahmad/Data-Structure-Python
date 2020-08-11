arr = []
n = int(input("Enter size of the array: "))
for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)
print("The array is: ", arr)
item = int(input("Enter the element to search: "))
flag = 0
for i in arr:
    if arr[i] == item:
        flag = 1
        break
    else:
        flag = 0
if flag == 1:
    print("Element Found at position", i+1)
else:
    print("Element Not Found")
