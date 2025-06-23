 #Factorial (commented)
fact = int(input("Enter number to find factorial: "))
f = 1
for i in range(1, fact + 1):
     f *= i
print(f)

print("=======================================================================================")

 #Bill Program
c = []  # List to store item prices

while True:
    print('''
      1. Create Bill
      2. Display Item Prices and Total Bill Amount
      3. Display Total
      4. Exit
      ''')

    ch = int(input("Enter choice (1-4): "))
    if ch == 1:
     while True:
         item = int(input("Enter price of item (0 to stop): "))
         if item == 0:
             break
         c.append(item)
         print(c)
    elif ch == 2:
     total = 0
     print("Final list is:", c)
     for m in c:
         total += m
     print("Total is:", total)

    elif ch == 3:
     total = 0
     for m in c:
        total += m
     print("Total amount of bill is:", total)

    else:
     print("Exiting the menu.")
print("=======================================================================================")
#max and min
p=[]
while True:
    num = int(input("enter list numbers"))
    if num == 0:
        break
    p.append(num)
print(p)
max_1=p[0]
min1=p[0]
for j in p:
    if j>max_1:
        max_1=j
        print("maximum is",max_1)
    if j<min1:
        min1=j
        print("minimum is",min1)