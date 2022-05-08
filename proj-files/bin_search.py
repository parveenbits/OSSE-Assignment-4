def binary_search(arr, low, high, x):
 
    #if high >= low
    if high >= low:
        #get the middle item
        mid = (high + low) // 2
 
        #check if item at middle
        if arr[mid] == x:
            return mid
 
        
        #else make recursive call on left
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        #othewise make recursive call on right
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        #else return -1 if item not found.
        return -1
 

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")