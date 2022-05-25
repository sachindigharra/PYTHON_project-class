from itertools import count
a=eval(input('enter the list'))
dct={}
for i in range(len(a)):
    x=a[i]
    y=a.count(a[i])
    dct[x]=y
print(dct)