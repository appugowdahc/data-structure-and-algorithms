def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        current_ele = arr[i] #we are taking back up current element 
        j = i-1
        
        while j>= 0 and current_ele < arr[j]:
            #we are just swaping the adjucent elements
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = current_ele
    
arr = [99,2,88,100,3,44,33,10,11,8]
insertion_sort(arr)
print(arr)
