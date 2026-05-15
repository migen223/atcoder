import sys
v,a,b,c=map(int,input().split())

people=[a,b,c]
dic={0:"F",1:"M",2:"T"}
while True:
    for i in range(3):
        if v-people[i]<0:
            print(dic[i])
            sys.exit()
        else:
            v-=people[i]
