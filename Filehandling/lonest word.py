with open('sachin.txt','r') as f:
    b={}
    data=f.read().split()
    print(data)
    print(len(data))
    print(max(data,key=len))
