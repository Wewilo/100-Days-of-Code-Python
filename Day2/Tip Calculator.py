print("Hey sir dont you want to give some tip?")

total_bill = float(input("What was the total bill? :"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? : "))

person = int(input("How many people to split the bill? : "))

total_cost = total_bill * tip / 100

split_cost = (total_bill + total_cost) / person  

print(f"Each person should pay: ${split_cost:.2f}")
