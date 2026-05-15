r=input()
if len(r)>=2:
    mod=r[-2]+r[-1]
    two=int(mod)
    print(100-two)
else:
    print(100-int(r))