import csv

# Data
data = [
    ["Name", "Address", "Mobile", "Email"],
    ["ab", "123 ", "999999999", "ab.com"],
    ["bc", "456 ", "8888888888", "bc.com"],
    ["cd", "789", "777777777", "cd.com"]
]

# Create CSV
with open("data2.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(" data2.csv created!")
