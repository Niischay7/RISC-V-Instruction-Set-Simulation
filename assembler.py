program_counter=0
def complement(binarynumber):
    ans = ""
    while binarynumber and binarynumber[-1] != "1":
        ans = binarynumber[-1] + ans
        binarynumber = binarynumber[0:-1]
    ans = binarynumber[-1] + ans
    binarynumber = binarynumber[0:-1]

    while binarynumber:
        if binarynumber[-1] == "0":
            ans = "1" + ans
        elif binarynumber[-1] == "1":
            ans = "0" + ans
        binarynumber = binarynumber[0:-1]
    return ans

def decimal_binary_32bits(b):
    a=int(b)
    if a>0:
        ans=""
        cnt=0
        while(a!=0):
            ans = str(a%2)+ans
            a = a//2
            cnt+=1
        ans="0"*(32-cnt)+ans
        return ans
    elif a==0:
        answer=32*"0"
        return answer
    elif a<0:
        a=abs(a)
        ans=""
        cnt=0
        while(a!=0):
            ans = str(a%2)+ans
            a = a//2
            cnt+=1
        ans="0"*(32-cnt)+ans
        ans=complement(ans)
    return ans

