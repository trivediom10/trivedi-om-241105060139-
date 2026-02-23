print("Performance Growth Comparator")
years = int(input("Enter years: "))
value1 = int(input("Enter first investment: "))
value2 = int(input("Enter second investment: "))
i = 1
while i <= years:
value1 = value1 + value1 * 8 / 100
value2 = value2 + value2 * 10 / 100
print("Year", i)
print("Investment1:", value1)
print("Investment2:", value2)
i = i + 1
if value1 > value2:
    print("Investment1 better")
    elif value2 > value1:
    print("Investment2 better")
    else
    print("Both equal")
    difference = value2 - value1
    print("Difference:", difference