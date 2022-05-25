import numpy as np
n=int(input())
a=list(map(int,input().split()))
b=list(reversed(a))
arr=np.array(b,dtype=float)
print(arr)
