n=int(input())
cube=[]
for i in range(1,1000000):
    cube.append(i*i*i)
def check(s):
    count=0

    for i in range(len(s)//2):
        if s[i]==s[-1-i]:
            count+=1
    if count==len(s)//2:
        return True
    else:
        return False
kaibun=[]
for i in cube:
    if check(str(i)):
        kaibun.append(i)

for i in range(len(kaibun)):
    #print(kaibun[-i-1])
    if n>=kaibun[-i-1]:
        print(kaibun[-i-1])
        break
        


