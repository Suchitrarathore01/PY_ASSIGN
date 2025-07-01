
import numpy as np

import matplotlib.pyplot as plt

#question 1
a=np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
print(a)
a1=np.nan_to_num(a,copy=True,nan=0.0)
print(a1)
#column
a1[:, [0, 1]] = a1[:, [1, 0]]
a1[:, [2, 3]] = a1[:, [3, 2]]
a1[:, [1, 3]] = a1[:, [3, 1]]
print(a1)
a1[[0, 1]] = a1[[1, 0]]  # row
print(a1)
#question 2
print("==========================================================")
b=np.array([[[3,4,5],[6,7,8]],[[1,4,0],[-1,-5,-6]]])
print(b)
print(b.shape)
b=np.transpose(b,(1,2,0))
print(b)
print(b.shape)
print("==========================================================")
#question 3
c_avg=np.nanmean(a,axis=0)
a2=np.nan_to_num(a,nan=c_avg)
print(a)
print(a2)
print("==========================================================")
#question 6
d=np.array([1,2,3])
d1=np.array([78,98,44])
d3=np.median(np.concatenate((d,d1)))
print("average",(d+d1)/2)
print("median",np.median(d3))
print("==========================================================")
#question 7
e1=np.array([[1,2,5],[0,8,6]])
e2=np.array([[8,3,4],[6,0,0]])
print("mean: ",np.mean((np.concatenate((e1,e2)))))
print("median: ",np.median((np.concatenate((e1,e2)))))
print("==========================================================")
#question 8
u=np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
print("matrix first\n",u)
v=np.array([9,-6,17])
print("matrix second\n",v)
m=np.linalg.solve(u,v)
print("solution:\n ",m)
u_inv=np.linalg.inv(u)
print("inverse of first\n",u_inv)
res=u_inv.dot(v)
print("inverse:\n ",res)
print("=============================================================")
#question 9
sem1 = np.array([90, 80, 70, 60, 55])
sem2 = np.array([90, 80, 85, 99, 100])
subjects = np.arange(5)
bar_width = 0.35
x1 = subjects
x2 = subjects + bar_width
plt.bar(x1, sem1, width=bar_width, label='Sem 1', color='cyan')
plt.bar(x2, sem2, width=bar_width, label='Sem 2', color='purple')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.title('Comparison of Sem 1 and Sem 2 Marks')
plt.legend()
plt.grid(True,axis='y', alpha=0.3,color='grey')
plt.show()









