from itertools import product
n=int(input())

def check(s):
    score=0
    for a in s:
        if a=="(":
            score+=1
        else:
            score-=1
        if score<0:
            return False
    if score==0:
        return True
    else:
        return False
    #上４行はreturn score==0 だけでかける
            


if n%2==0:
    for a in product(["(",")"],repeat=n):
        if check("".join(a)):
            print("".join(a))
        

