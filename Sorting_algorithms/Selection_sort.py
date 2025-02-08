def Selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
arr = [99,2,88,100,3,44,33,10,11,8]
Selection_sort(arr)
print(arr)
