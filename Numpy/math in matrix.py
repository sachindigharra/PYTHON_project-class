import numpy as np
m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
m1=np.array(l1.reshape(m,n))
m2=np.array(l2.reshape(m,n))
out1=np.add(m1,m2)
out2=np.subtract(m1,m2)
out3=np.divide(m1,m2)
out4=np.mulity(m1,m2)
out5=np.power(m1,m2)
