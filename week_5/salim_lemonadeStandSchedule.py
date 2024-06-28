"""
Author: Meher salim
Date: 06/27/2024
File Name: salim_lemonadeStandSchedule.py
Description: Build a Python program that manages weekly schedule for a lemonade stand.
"""

# Define list of 5 tasks related to running a lemonade stand
tasks = ["Buy ingredients", "Make lemondafe", "Sell lemonade", "Count earnings", "Clean up"]

# Use for loop to iterate over the list of tasks and print them to console window
print("Lemonade Stand Tasks:")
for task in tasks:
  print(task)

# Define days of the week (Sunday - Saturday)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Use for loop to iterate over the list of days
for i, day in enumerate(days):
  # Add if/else statment to display the task for each day
  if day == "Saturday" or day == "Sunday":
    print(f"{day} is a day off, time to rest!") # Print special message for Saturday and Sunday
  else:
    print(f"{day}: {tasks[i % len(tasks)]}") # Use modulo to cycle through tasks