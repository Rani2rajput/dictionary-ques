dic="MISSISSIPI"
d={}
for i in dic:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)