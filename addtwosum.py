def addtwonum(list1,list2):
    s=""
    s1=""
    for i in range(len(list1)):
        s=s+str(list1[i])
    for i in range(len(list2)):
        s1=s1+str(list2[i])
    sum=int(s)+int(s1)
    reversedsum=str(sum)
    rv1=reversedsum[::-1]
    x=[*rv1]
    return x
