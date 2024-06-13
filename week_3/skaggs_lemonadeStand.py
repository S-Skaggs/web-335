"""
Author: Sheldon Skaggs
Date: 6/13/2024
File Name: lemonadeStand.py
Description: This Python solution will calculate cost and profit for a lemonade stand
"""

# Calculate the cost of making the lemonade.
def calculate_cost(lemons_cost, sugar_cost):
    return float(lemons_cost) + float(sugar_cost)

# Calculate the profit for the lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    totalCost = calculate_cost(lemons_cost, sugar_cost)
    netProfit = float(selling_price) - float(totalCost)
    return netProfit

# Declare and assign variables
lemons_cost = 1.50
sugar_cost = 1.25
selling_price = 5

# Declare variables to hold calculated output
total_cost = calculate_cost(lemons_cost, sugar_cost)
net_profit = calculate_profit(lemons_cost, sugar_cost, selling_price);

# Print the formatted results
print ("Costs")
print (f"{lemons_cost} + {sugar_cost} = {total_cost}")
print ()
print ("Net Profit")
print (f"{selling_price} - {total_cost} = {net_profit}")