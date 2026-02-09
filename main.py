sales = float(input("Enter total sales today: "))
expenses = float(input("Enter total expenses today: "))

profit = sales - expenses

file = open("records.txt", "a")
file.write(f"Sales: {sales}, Expenses: {expenses}, Profit: {profit}\n")
file.close()

print("\n----- Daily Business Report -----")
print("Sales:", sales)
print("Expenses:", expenses)

if profit > 0:
    print("Profit:", profit)
elif profit < 0:
    print("Loss:", abs(profit))
else:
    print("No profit, no loss")

print("\nRecord saved successfully.")

total_sales = 0
total_expenses = 0
total_profit = 0
with open("records.txt", "r") as file:
    for line in file:
        parts = line.split(",")

        sale = float(parts[0].split(":")[1])
        expense = float(parts[1].split(":")[1])
        prof = float(parts[2].split(":")[1])

        total_sales += sale
        total_expenses += expense
        total_profit += prof

print("\n----- Monthly Summary -----")
print("Total Sales:", total_sales)
print("Total Expenses:", total_expenses)
print("Net Profit:", total_profit)
