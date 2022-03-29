num={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dic=list(num.values())
dic.sort()
dic1={}
for i in dic:
    for j in num:
        if i==num[j]:
            dic1[j]=i
print(dic1)