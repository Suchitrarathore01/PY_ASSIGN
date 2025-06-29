import numpy as np
#question 1 of assignment 9
a=np.array([[1,2,3,4],[90,70,60,50]])
b=np.array([9,8,7,6,9,0,7,0])
combine=np.concatenate((b,a.ravel()))
print(combine)
print("=======================================")
#question 2 of assignment 9
c=np.array([[1,2,3,4],[90,70,60,50]])
c=c.flatten()
print(c)
print("=======================================")
#question 3 of assignment 9
d=np.array([9,8,7,6,9,0,7,0])
print(d[::-1])
#question 4 of assignment 9
print("=======================================")
e=np.array([[1,2,3,4],[90,70,60,50]])
print(e)
print(e.max())
print("=======================================")
print(e.min())
print("=======================================")
print(e.shape)
print("=======================================")
for i in e:
    print(i)
    for j in i:
        print(j)
print("=======================================")
sum1=0
for x in e:
    for y in x:
        sum1 +=y
print(sum1)
print("=======================================")
u=np.array([[[1,2,3,4],[90,70,60,50]],[[4,5,6,7],[20,21,22,23]]])
v=np.array([[[1,2,3,2],[90,70,60,50]],[[4,5,6,7],[20,21,22,23]]])
print(f" 1st array {u}\n")
print(f"2nd array {v}\n")
print("addition\n",u+v)
print("subtraction\n",u-v)
print("multiplication\n",u*v)
print("division\n",u/v)





