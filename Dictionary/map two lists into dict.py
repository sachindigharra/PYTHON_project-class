from multiprocessing import Value


key=['name','section','uni.roll','roll.no','c.pi','girl friend']
Value=['sachin','Q','2115000886','44','7.40']
dct=dict(zip(key,Value))
print(dct)