#Q10

hall_rental = int(input("hall rent"))
decorations = int(input("decoration cost"))
food_cost_per_person = int(input("food cost per person"))
guest_num = int(input("number of guests"))
sound_system_rental = int(input("sound system rental"))

total_food_cost = food_cost_per_person * guest_num
total_budget = (hall_rental) + (decorations) + (total_food_cost) + (sound_system_rental)

print("total event budget =",total_budget)
