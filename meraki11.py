dic= {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0 
for i in dic:
    if dic[i]>max1:
        max3==max2
        max2=max1
        max1=dic[i]
    elif dic[i]>max2:
        max3=max2
        max2=dic[i]
    elif dic[i]>max3:
        max3=dic[i]
print(max1,max2,max3)