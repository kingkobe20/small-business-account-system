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
