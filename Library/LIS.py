from bisect import bisect_left

#狭義単調増加のLIS
#ans[i]:i+1の長さのLISを作る時の末尾の最小値
def LIS(l):
    n=len(l)
    ans=[2**61-1]*(n+1)
    for i in range(n):
        ind=bisect_left(ans,l[i])
        ans[ind]=l[i]
    while ans[-1]==2**61-1:
        ans.pop()
    return ans 

l=[1,3,2,1,4,6,2,4]
print(LIS(l))

    