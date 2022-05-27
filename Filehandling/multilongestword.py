with open('sachin.txt','r') as f:
    data=f.read().split()
    b=[]
    print(data)
    print(len(data))
    c=max(data)
    print(c)
    for i in data:
        if len(i)==len(c):
            b.append(i)
    print(b)
