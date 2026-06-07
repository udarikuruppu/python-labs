#Q8

data_usage = float(input("data usage in GB"))
cost_per_GB = int(input("cost per GB"))
service_charges = int(input("additional service chargers"))

data_cost = data_usage * cost_per_GB
final_cost = (data_cost) + (service_charges)

print("data cost =",data_cost)
print("additional chargers=",service_charges)
print("final bill =",final_cost)
