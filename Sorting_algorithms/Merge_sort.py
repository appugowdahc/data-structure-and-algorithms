def merge(l,b,sub_arr):
    i=j=k = 0
    while i < len(l) and j <len(b):
        if l[i] <= b[j]:
            sub_arr[k] = l[i]
            i += 1
        else:
            sub_arr[k] = b[j]
            j += 1
        k += 1
    while i< len(l):
        sub_arr[k] = l[i]
        i += 1 
        k += 1
    while j < len(b):
        sub_arr[k] = b[j]
        j+= 1
        k += 1
    
def merge_sort(sub_arr):

    if len(sub_arr) > 1:
          
        mid = len(sub_arr) //2
        l = sub_arr[:mid]
        r = sub_arr[mid:]
        merge_sort(l)
        merge_sort(r)
        merge(l,r,sub_arr)




arr = [9,3,22,55,33,55,34,23,88,9,10,7,6]
merge_sort(arr)
print(arr)
