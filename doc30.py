a={"s 001":["math","science"],"s 002":["math","english"]}
d={}
for i,j in a.items():
    for x in " ":
        i=i.replace(x,"")
        d[i]=j
print(d)