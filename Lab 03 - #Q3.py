#Q3

distance = float(input("distance traveled"))
fuel_efficiency = float(input("fuel efficiency"))
price_per_liter = float(input("fuel price per liter"))
highway_charges = int(input("highway charges"))

fuel_used = distance/fuel_efficiency
fuel_cost = fuel_used*price_per_liter
final_trip_cost = (fuel_cost) + (highway_charges)

print("fuel used =",fuel_used)
print("fuel cost =",fuel_cost)
print("final trip cost =",final_trip_cost)
