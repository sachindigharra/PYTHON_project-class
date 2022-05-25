a={}
num=int(input('enter the range of dictionary'))
for i in range(0,num):
    x=int(input('enter key'))
    y=int(input('enter the value'))
    a[x]=y
h=a.values()
print(min(h))
print(max(h))