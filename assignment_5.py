# question 1 assignment5
import pandas as pd
fruits={1:"mango",2:"apple",3:"pear"}
f1=pd.Series(fruits)
print(f1[1])
color=["red","pink","blue"]
f2=pd.Series(color,index=["m","a","p"])
print(f2)
print(f2["a"])
#question 2 for assignment5
data={"roll_no":[1,2,3],"class":[12,11,10]}
f3=pd.DataFrame(data)
print(f3)
l=[[6,7,8],[5,9,10]]
f4=pd.DataFrame(l,index=[89,98])
print(f4)
t=(("a","b","c"),("m","n","o"))
f5=pd.DataFrame(t)
print(f5)
l2=[{5:"f",6:"j",7:"k"},{"i":"u","l":"m","h":"g"}]
f6=pd.DataFrame(l2)
print(f6)
#question 3 of assignment5
print(f3.loc[0])
print(f3.loc[[0,1]])
print(f4.loc[89])
df=pd.DataFrame([['l','m'],['l','m'],['l','m'],['l','m']],columns=['col_l','col_m'])
print(df)
x=df.iloc[1:3,:]
print(x)
# y=df.loc[1:3,'col_l']
# print(y)
res=df[df['col_l']==0]
print(res)
df.iloc[1]=['y','z']
rows_list=df.values.tolist()
print(rows_list)

