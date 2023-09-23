def zigZag(arr):
        mid=(len(arr)-1)//2
        for i in range(mid):
            temp=0
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
        
        for i in range(mid+1,len(arr)):
            temp=0
            if arr[mid+1]>arr[mid+2]:
                temp=arr[mid+1]
                arr[mid+1]=arr[mid+2]
                arr[mid+2]=temp
                
        for i in range(len(arr)):
            if arr[i]<arr[i+1] and arr[i+1]>arr[i+2]:
                return 1
            else:
                return 0
                
