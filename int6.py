test_str ="mynameeeeisrani21"
a = {}
c=0
for i in test_str:
    if i in a :
        a[i] += 1

    elif i in " ":
        c=c+1
         
    else:
        a[i] = 1
        
#b = max(a, key = a.get) 
print ("The maximum chr is name:",str(a))
print("total space is",c)