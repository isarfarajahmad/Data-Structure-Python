arr = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    x = int(input("Enter the element: "))
    arr.append(x)
print("The array is:", arr)
arr.sort()
print("Array after sorting:",arr)
item = int(input("Enter the element to search: "))
l = 0
u = n-1
while l <= u:
    mid = (l+u) // 2
    if arr[mid] == item:
        print("Element Found at position", mid+1)
        break
    elif arr[mid] < item:
        l = mid +1
    else:
        u = mid -1
