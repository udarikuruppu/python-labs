#Q6

monthly_fee = int(input("monthly fee"))
num_month = int(input("number of months"))
registration_fee = int(input("registration fee"))
trainer_fee = int(input("personal trainer fee"))
tax_percentage = float(input("tax percentage"))

total_before_tax = (monthly_fee * num_month) + (registration_fee + trainer_fee)
tax = total_before_tax*tax_percentage/100
final_payment = (total_before_tax) - (tax)

print("total before tax =", total_before_tax)
print("tax =",tax)
print("final payment =", final_payment)
