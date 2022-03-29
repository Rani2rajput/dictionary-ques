x={"a":[4,5,6],"b":[7,8,9]}
list1=[]
for i in x:
    list1.append(x[i])
    for j in list1:
       sum=0
       for k in j:
          sum+=k
          x[i]=sum
print(x)
    
    
        
        