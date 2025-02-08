def reverse(arr,start,end):
    no_count = end-start+1
    count = 0
    while(no_count//2 != count):
        # print(start,end)
        arr[start+count],arr[end-count] = arr[end-count],arr[start+count]
        count +=1

def rotate_arr(arr,l,d):
   start = 0
   end = l-1
   reverse(arr,start,end)
   
   start = 0
   end = l-d-1
   reverse(arr,start,end)
   
   start = l-d-1
   end = l-1
   reverse(arr,start,end)


arr = [1,2,3,4,5,6,7,8,9]
d = 3
l = len(arr)
rotate_arr(arr,l,d%l)
print(arr)
