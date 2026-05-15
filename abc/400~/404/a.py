s=input()
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in l:
    if i in s:
        continue
    else:
        print(i)
        break