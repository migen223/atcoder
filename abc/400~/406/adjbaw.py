a_list=[1,2,3]
b_list=[4,5,6,7]
ab=[]

if len(a_list)>=len(b_list):
        for j in range(len(a_list)-1):
            ab.append(a_list[j])
            ab.append(b_list[j])
        ab.append(a_list[len(a_list)-1])
else:
    for j in range(len(b_list)-1):
        ab.append(b_list[j])
        ab.append(a_list[j])
    ab.append(b_list[len(b_list)-1])
print(ab)