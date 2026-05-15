
t=int(input())

def tostr(n,s):
    ans=""
    for i in range(n-len(s)):
        ans+="0"
    ans+=s
    return ans

def ten_to_n(num,n):#numをn進数に変換　返り値はstr
    if num==0:
        return "0"
    else:
        k=0
        while n**k<=num:
            k+=1
        ans=[]
        rang=k
        for i in range(rang):
            k-=1
            keta=num//(n**k)
            num-=keta*(n**k)
            ans.append(str(keta))
        return "".join(ans)

def n_to_ten(num,n):#num(n)を10進数に変換　返り値はstr
    s=str(num)
    ans=0
    k=0
    for i in range(len(s)):
        ans+=int(s[-1-i])*n**k
        k+=1
    return str(ans)

for _ in range(t):
    n=int(input())
    s=input()

    number=[0]*(2**n)
    number[0]=1
    """
    for i in range(2**n):
        st=tostr(n,ten_to_n(i,2))
        print(st)
    """
    for i in range(2**n-1):
        st=tostr(n,ten_to_n(i,2))
        #print(st)
        if number[i]==1:
            #st=ten_to_n(i,2)
            for j in range(n):
                if st[j]=="0":
                    #print(f"ijsdx {i+2**(n-j-1)}")
                    if s[i+2**(n-j-1)-1]=="0":
                        
                        number[i+2**(n-j-1)]=1
        #print(f"st={st}")
        #print(number)
    if number[2**n-1]==1:
        print("Yes")
    else:
        print("No")

             
    

 

        
