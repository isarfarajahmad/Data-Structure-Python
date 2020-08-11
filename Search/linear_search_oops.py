pos = 0
def search_while(arr, item):
    i = 0
    while(i<len(arr)):
        if arr[i] == item:
            globals() ['pos'] = i
            return True
        i += 1
    return False

def search_for(arr, item):
    for n in range(len(arr)):
        if arr[n] == item:
            globals() ['pos'] = n
            return True
    return False

arr = [10,20,30,40,50]
item = 30
if search_while(arr, item):
    print('Found at position', pos+1)
else:
    print('Not found')

if search_for(arr, item):
    print('Found at position', pos+1)
else:
    print('Not found')