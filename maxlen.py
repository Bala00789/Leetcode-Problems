def maxLen(n, arr):
        #Code here
        for i in range(n):
            for j in range(1,n):
                zero=arr[i]+arr[j]
                if zero==0:
                    return j
