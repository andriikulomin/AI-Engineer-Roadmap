bread_sold = int(input("How much bread did we sell? ")) # Asking for amount
milk_sold = int(input("How much milk did we sell? "))
cheese_sold = int(input("How much cheese did we sell? "))
bread_price = 3
milk_price = 2
cheese_price = 2
total_income = (bread_sold * bread_price) + (milk_sold * milk_price) + (cheese_sold * cheese_price) # Counting total income
staff = 200
electricity = 100
security = 200
expenses = staff + electricity + security
net_income = total_income - expenses # Counting net income
print("Total income: " + str(total_income))
print("Net income: " + str(net_income))