def np(n,arr):
    i=0
    while i<=n:
        if arr[i]<arr[i+1]:
            i=i+1
        else:
            break
    while i<=(n-1):
        if arr[i]>arr[i+1]:
            temp=arr[i+1]
            arr[i+1]=arr[i]
            arr[i]=temp
    return arr
