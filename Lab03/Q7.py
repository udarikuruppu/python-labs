#Q7

modules = int(input("number of modules"))
fee_per_module = int(input("fee per module"))
library_fee = int(input("library fee"))
registration_fee = int(input("registration fee"))

total_module_fee = modules*fee_per_module
full_payment = (total_module_fee) + (library_fee) + (registration_fee)

print("total module fee =",total_module_fee)
print("full payment =",full_payment)
