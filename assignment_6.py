import pandas as pd
#question 1 assignment 6
d=pd.to_datetime(["2025-09-08","2025-09-08","2025-09-08","2025-09-08"])
print(d)
# question 2 of assignment 6
df1=pd.DataFrame({"car":["aa","cc","bb"],"price":[90,88,66],"id":[1,2,3]})
df2=pd.DataFrame({"car":["ss","tt","rr"],"price":[56,88,66],"id":[1,2,3]})
print(df2.merge(df1,how="inner",on='price'))
print(df2.merge(df1,how="inner",on='id'))
#print(pd.merge(df1,how="inner",on='id'))
ress=df2.join(df1,rsuffix="_right",lsuffix="_left")
print(ress)
#question 3 of assignment 6
df4=pd.DataFrame({"car":["aa","cc","bb"],"price":[90,88,66],"id":[1,2,3]})
df5=pd.DataFrame({"car1":["ss","tt","rr"],"price":[56,88,66],"id":[1,2,3]})
df7=pd.concat([df4,df5],keys=["a1","a2"],axis=1)
df9=pd.concat([df4,df5])
print(df9)
df8=df4.merge(df5,how="inner",on='id')