#Q4

basic_salary = int(input("enter basic salary"))
overtime_hours = int(input("overtime hours"))
overtime_rate = float(input("overtime rate"))
bonus = int(input("bonus"))
tax_percentage = float(input("tax percentage"))

gross_salary = (basic_salary) + (overtime_hours * overtime_rate) + (bonus)
tax_amount = gross_salary * tax_percentage/100
net_salary = (gross_salary) - (tax_amount)

print("gross salary =",gross_salary)
print("tax amount =",tax_amount)
print("net salary =",net_salary)
