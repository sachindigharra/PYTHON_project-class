import numpy as np
def transpose_array(row,column):
    a=[]
    d=[]
    for i in range(row):
        b=list(map(int,input().split()))
        a.append(b)
        for j in range(len(b)):
            d.append(b[j])
    c=np.zeros([column,row])
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j]=a[j][i]
    c=np.array(c,dtype=int)
    d=np.array(d)
    print(c)
    print(d)
row,column=map(int,input().split())
result_list=transpose_array(row,column)
