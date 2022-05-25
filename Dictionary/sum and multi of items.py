a={1:2,2:3,3:4,5:9}
s=0
p=0
for i,j in a.items():
    p=i+j
    s+=p
print('sum of items',s)
#multiple of items
s=1
p=0
for i,j in a.items():
    p=i*j
    s*=p
print('the multiple of items',s)
