bread_sold = int(input())
milk_sold = int(input())
cheese_sold = int(input())
bread_cost = 3
milk_cost = 2
cheese_cost = 2
total_income = (bread_sold * bread_cost) + (milk_sold * milk_cost) + (cheese_sold * cheese_cost)
staff = 200
electricity = 100
security = 200
work_out_come = staff + electricity + security
net_income = total_income - work_out_come
print("Total income: " + str(total_income))
print("Net income: " + str(net_income))