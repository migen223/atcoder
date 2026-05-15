
s=input()
p=10**9+7

word={"c":0,"h":1,"o":2,"k":3,"u":4,"d":5,"a":6,"i":7}

dic={}
for i in range(8):
    dic[i]=0
ns=[]
for i in range(len(s)):
    if s[i] in word:
        ns.append(word[s[i]])

for i in range(len(ns)):
    if ns[-i-1]==7:
        dic[7]+=1
    else:
        dic[ns[-i-1]]+=dic[ns[-i-1]+1]
print(dic[0]%p)
