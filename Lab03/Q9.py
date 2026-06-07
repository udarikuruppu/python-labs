#Q9

adult_ticket_price = int(input("adult ticket price"))
num_adults = int(input("number of adults"))
child_ticket_price = int(input("child ticket price"))
num_children = int(input("number of children"))
snack_package = int(input("snack package cost"))

total_price_adult = adult_ticket_price*num_adults
total_price_child = child_ticket_price*num_children
full_cost = (total_price_adult) + (total_price_child) + snack_package

print("price for adults =",total_price_adult)
print("price for children =",total_price_child)
print("snack package price =",snack_package)
print("full cost =",full_cost)
