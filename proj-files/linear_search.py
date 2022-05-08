def search(arr, x):

    #for a range of numbers check each element
    for i in range(len(arr)):
        #if found, return the position
        if arr[i] == x:
            return i
  
    return -1