dic={"v":[5,7,6],"vi":[8,4,9],"vii":[1,9,6]}
d=[]
for i in dic:
    dic[i].sort()
    d.append(i)
    d.append(dic[i])
print(d)
    