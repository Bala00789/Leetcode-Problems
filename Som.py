def subArraySum(arr,s):
    elements=[]
    j=0
    for i in range(len(arr)):
        limit=0
        j=j+1
        for j in range(len(arr)):
            limit=limit+arr[j]
            if limit==s:
                return limit
            else:
                break
            
        
