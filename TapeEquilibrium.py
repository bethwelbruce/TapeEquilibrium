def solution(A):
    if len(A)< 2:
        return 0
    s = sum(A)
    mindiff = 2000
    SL=0
    for i in range(0,len(A)-1):
        SL+=A[i]
        diff = abs(2*SL-s)
        mindiff=min(mindiff,diff)

    return mindiff