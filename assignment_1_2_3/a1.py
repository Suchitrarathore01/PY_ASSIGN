name=input("enter your name")
class_1=int(input("enter your class"))
m_1=int(input("enter your marks of english"))
m_2=int(input("enter your marks of maths"))
m_3=int(input("enter your marks of hindi"))
m_4=int(input("enter your marks of sst"))
m_5=int(input("enter your marks of evs"))
total_marks = m_1 + m_2 + m_3 + m_4 + m_5
per = (total_marks / 500) * 100
print(f"name of student is {name} and class is {class_1}")
print(f" percentage of student is {per:.3f}")
if per >=80:
    print("A GRADE")
elif per<80 and per >60:
    print (" B GRADE")
else:
    print ("C GRADE")
print("-------------------------------------------------------------------------------------")
# second question
name_1=input("enter your first name")
name_2 = input("enter your last name")
f_name = name_1+name_2
print(f_name)
print(f_name.upper())
print(f_name.lower())
print(f_name.capitalize())
print(f_name.startswith("h"))
print(f_name.endswith("h"))
print(f_name.replace(name_1,"alice"))
print(f_name.split(" "))
print(f_name.find("s"))
print(f_name.rfind("t"))
print(f_name.count("s"))

