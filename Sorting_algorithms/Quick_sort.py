def swap(arr,left,right):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp
    
def quicksort(arr,start,end):
    pivot = start
    left = start
    right = end
    while left < right:
        while left < end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        if left < right:
            swap(arr,left,right)
    swap(arr,pivot,right)
    return right
def partition(arr,start,end):
    if start < end:
        p_idx = quicksort(arr,start,end)
        partition(arr,start,p_idx-1)
        partition(arr,p_idx+1,end)


arr = [4,90,100,111,2,1,10,113,10]
partition(arr,0,len(arr)-1)
print(arr)