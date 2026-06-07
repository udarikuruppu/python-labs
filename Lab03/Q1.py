#Q1
room_charge = float(input("room charge per day"))
days = int(input("Number of days"))
food_charge = float(input("Food chargers"))
service_charge_percentage = float(input("service charge percentage"))

subtotal = (room_charge * days) + (food_charge) 
service_charge = (subtotal) * (service_charge_percentage)/100
final_bill = (subtotal) + (service_charge)

print(" subtotal is ", subtotal)
print(" service charge is ", service_charge)
print(" final bill = ", final_bill)
