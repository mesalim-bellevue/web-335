"""
Author: Meher Salim
Date: 06/014/2024
File Name: salim_lemonadeStandSchedule.py
Description: Simulate a lemonade stand by calculating cost and profit of making and selling lemonade.
"""

# variables to test each function
lemons_cost = 1.5 # cost of lemons
sugar_cost = 0.2 # cost of sugar
selling_price = 8 # selling frice of lemonade

# define the function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
  total_cost = lemons_cost + sugar_cost # calculate total cost
  return total_cost # return total cost of making lemonade

# define the function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
  total_cost = calculate_cost(lemons_cost, sugar_cost) # use calculate_cost fucntion to get total cost
  profit = selling_price - total_cost # calculate the profit
  return profit # return profit from selling lemonade

# use calculate_cost function
total_cost = calculate_cost(lemons_cost, sugar_cost)
cost_output = f"Cost of lemons: ${lemons_cost} + Cost of sugar: ${sugar_cost} = Total cost: ${total_cost}" # calculate output of total cost
print(cost_output) # print the total cost

# use the calculate_profit function
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)
profit_output = f"Selling price: ${selling_price} - Total cost: ${total_cost} = Profit: ${profit}" # calculate profit output
print(profit_output) # print profit