n=int(input())
a=list(map(int,input().split()))
ans=[]
number_to_ind={}
ind_to_unmber={}
for i in range(n):
    number_to_ind[a[i]]=i
    ind_to_unmber[i]=a[i]
for i in range(1,n+1):
    if number_to_ind[i]!=i-1:
        ind=number_to_ind[i]
        c,d=number_to_ind[i],number_to_ind[ind_to_unmber[i-1]]
        e,f=ind_to_unmber[i-1],ind_to_unmber[c]
        number_to_ind[i],number_to_ind[ind_to_unmber[i-1]],ind_to_unmber[i-1],ind_to_unmber[c]=d,c,f,e
        #number_to_ind[i],ind_to_unmber[i-1],number_to_ind[ind_to_unmber[i-1]],ind_to_unmber[number_to_ind[i]]=i-1,i,number_to_ind[i],ind_to_unmber[i-1]
        ans.append([i,ind+1])
    #print(number_to_ind,ind_to_unmber)
#print(ans)
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

"""
for i in range(1,n+1):
    if number_to_ind[i]!=i-1:
        print(number_to_ind[i],number_to_ind[ind_to_unmber[i-1]],i-1,number_to_ind[i])
        number_to_ind[i],ind_to_unmber[i-1],number_to_ind[ind_to_unmber[i-1]],ind_to_unmber[number_to_ind[i]]=i-1,i,number_to_ind[i],ind_to_unmber[i-1]
        ans.append([i,number_to_ind[i]+1])
        """