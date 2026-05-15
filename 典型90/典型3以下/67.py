n,k=map(str,input().split())
def eightto(n):
    eight=[int(i) for i in n]
    e=0
    for i in range(len(eight)):
        e+=eight[len(eight)-i-1]*(8**i)
    return e


def tonine(e):
    count=0
    while True:
        if e==0:
            return ["0"]
        elif 9**count<=e<9**(count+1):
            break
        else:
            count+=1
    nine=[]
    for i in reversed(range(count+1)):
        for j in range(9):
            if j*9**i<=e<(j+1)*9**i:
                e-=j*9**i
                nine.append(str(j))
                break
    return nine

for _ in range(int(k)):
    ten=eightto(n)
    #print(f"ten={ten}")
    nine=tonine(ten)
    #print(f"nine={nine}")
    newnine="".join(nine).replace("8","5")
    n=newnine
    #print(f"n={n}")
    
print(newnine)



    
    