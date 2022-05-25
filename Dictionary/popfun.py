# pop() its used of delete the key:value pair baished to giev key  
a={}
num=int(input('enter the range'))
for i in range(0,num):
    x=input('enter key')
    y=input('enter value')
    a.update({x:y})
a.pop('2')
print(a)
# popitem() its used of delete from the last of dictionary
a={}
num=int(input('enter the range'))
for i in range(0,num):
    x=input('enter key')
    y=input('enter value')
    a.update({x:y})
a.popitem()
print(a)