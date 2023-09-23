def reverse(x):
        s=str(x)
        rnum=s[::-1]
        rlist=[*rnum]
        rlist1=[]

        if rlist[0]=="0":
            rlist.remove("0")
            s=""
            for i in range(len(rlist)):
                s=s+rlist[i]
            print(int(s))
        elif rlist[len(rlist)-1]=="-":
            rlist.remove("-")
            rlist1.append("-")
            rlist1=rlist1+rlist
            s=""
            for i in range(len(rlist1)):
                s=s+rlist1[i]
            print(int(s))
        
