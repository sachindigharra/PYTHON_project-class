with open('sachin.txt','r') as f:
    data=f.readlines()
    print(max(data,key=len))
