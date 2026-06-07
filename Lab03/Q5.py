#Q5

product1 = int(input("price"))
num_product1 = int(input("number of items"))
product2 = int(input("price"))
num_product2 = int(input("number of items"))
product3 = int(input("price"))
num_product3 = int(input("number of items"))
delivery = int(input("delivery charges"))
discount_percentage = float(input("discount percentage"))

gross_price = (product1*num_product1) + (product2*num_product2) + (product3*num_product3)
discount = gross_price * discount_percentage/100
total_bill = (gross_price) + (delivery)  - (discount)

print("gross price =",gross_price)
print("discount =",discount)
print("total price is",total_bill)
