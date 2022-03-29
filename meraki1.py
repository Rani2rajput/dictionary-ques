dict1={1:10,2:20}
dict2={3:30,2:40}
dict3={5:50,6:60}
m={}
for i in dict1:
    for j in dict2:
        for k in dict3:
            if i==j:
                m[j]=dict1[i]+dict2[j]
            else:
                m.update(dict1)
                m.update(dict2)
                m.update(dict3)
print(m)
           