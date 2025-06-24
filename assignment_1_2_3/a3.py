def calc(a,b):
    print("sum is",a+b)
    print("subtract is\n",a-b)
    if b!=0:
     print("division is\n",a/b)
     print("remainder is\n",a%b)
    else:
        print("this division is not possible")
x=int(input("enter number 1\t"))
y=int(input("enter number 2\t"))
calc (x,y)  
print("=================================================================================")
num1=int(input("enter number to check palindrome"))
reverse=0
temp=num1
while num1>0:
    rem=num1%10
    reverse=reverse*10+rem
    num1=num1//10
if reverse==temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome number")
    


