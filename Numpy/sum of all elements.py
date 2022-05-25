import numpy as np
arr1=np.arange(1,10,2)
arr2=np.arange(11,20,2)
print(len(arr1),len(arr2))
if len(arr1) == len(arr2):
    sum=0
    for i in range(len(arr1)):
        sum+=(arr1[i]+arr2[i])
    print('sum of elements',sum)
else:
    print('sum is imposible')
