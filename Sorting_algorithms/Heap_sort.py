def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def max_heapify(arr,n,i):
    largest = i
    left = i*2+1
    right = i*2+2
    #parent = i-1//2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr,largest,i)
        max_heapify(arr,n,largest)
def min_heapify(arr,n,i):
    smallest = i
    left = i*2+1
    right = i*2+2
    #parent = i-1//2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        swap(arr,smallest,i)
        min_heapify(arr,n,smallest)
def heap_sort(arr):
    for i in range(len(arr)-1,0,-1):
        swap(arr,i,0)
        min_heapify(arr,i,0)
arr = [9,8,2,44,1,33,22,19,15,11]
n = len(arr)
for i in range(n//2-1,-1,-1):
    min_heapify(arr,n,i)
heap_sort(arr)
print("the sorted array is:",arr)

