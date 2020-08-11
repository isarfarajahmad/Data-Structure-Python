pos = 0
def search(arr, item):
    l = 0
    u = len(arr) - 1
    while l <= u:
        mid = (l+u) // 2
        if arr[mid] == item:
            globals() ['pos'] = mid
            return True
        else:
            if arr[mid] < item:
                l = mid + 1
            else:
                u = mid -1
    return False


arr = [3,4,5,6,7,8]
item = 7
if search(arr, item):
    print("Element found at position", pos+1)
else:
    print("Element not found")