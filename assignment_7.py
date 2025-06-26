# question 1 of assignment 7
import pandas as pd
#str.contains return boolean series
data=pd.DataFrame({'name':['siI','aLea@','ariE@','Jack','Lisa']})
f1=data[data['name'].str.contains(r'@',case=False,regex=True)]# case=False means A=a that is ignore case sensitivity
print(f1)
print("==============================================================")
#str.match return boolean series
f2=data[data['name'].str.match(r'^[al]')]# names starts with a or l
print(f2)
print("============================extract====================================")
extracted = data['name'].str.extract(r'([A-Z])([a-z]+)')
print(extracted)
print("==============================================================")
#str.extract returns dataframe not boolean value
data[['first','rest']] = data['name'].str.extract(r'([A-Z])([a-z]+)')
print(data)
#df[df[...]] only to filter rows
print("==============================================================")
#it is transforming
data['replaced']=data['name'].str.replace(r'[aeiou]','*',case=False,regex=True)
print(data)
print("=================================================================")
#for phone and email
df = pd.DataFrame({
    'email': ['abc@gmail.com', 'invalid@', 'mno@domain.co'],
    'phone': ['9876543210', '123456', '8123456789']
})
# Validate emails
df['valid_email'] = df['email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
# Validate phone numbers
#  ^ start of string $ end of string
df['valid_phone'] = df['phone'].str.match(r'^[0-9]\d{9}$')
print(df)
print("=================================================================")
#question 2 of assignment 7
date=pd.date_range('2025/01/02',periods=6)
print(date)
date=pd.DataFrame(date,columns=['date'])
print(date)
date['date']=pd.to_datetime(date['date'])
date['year']=date['date'].dt.year
date['month']=date['date'].dt.month
date['day']=date['date'].dt.day
date['weekday']=date['date'].dt.day_name()
print(date)
date_f=date[date['date']>'2025-01-05']
print(date_f)
today=pd.to_datetime("today")
date['diff']=today-date['date']
print(date)
print("=======================================================")
#question 3 of assignment 7
dc=pd.read_csv('new_data_3.csv')
print(dc)
print(pd.options.display.max_rows)
print(dc.shape)
new_dc=dc.dropna()
print(new_dc.to_string())
print(dc.fillna(10,inplace=True))
print(dc.fillna({'Index':10},inplace=True))
x=dc['Index'].mean()
print(x)
y=dc['Index'].median()
print(y)
z=dc['Index'].mode()[0]
print(z)


