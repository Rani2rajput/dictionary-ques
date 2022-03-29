def fun(l):
    dic={}
    for k,v in l:
        dic.setdefault(k,[]).append(v)
    return dic
colours=[("yellow",1),("blue",2),("yellow",3),("blue",4)("red",1)]
print(fun(colours))