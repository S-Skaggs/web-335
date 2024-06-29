"""
Author: Sheldon Skaggs
Date: 6/28/2024
File Name: Skaggs_lemonadeStandSchedule.py
Description: This Python solution will help manage the schedule for the lemonade stand
"""

# Create variables to hold tasks and days
lemonadeStandTasks = ["Buy lemons and sugar", "Make lemonade", "Sell lemonade", "Count earnings", "Clean stand and equipment"]
daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Create a variable to hold the day's task index
dayTaskIndex = 0

# Iterate over our tasks and print them to the screen for verification
for task in lemonadeStandTasks:
    # print the task
    print(task)

for day in daysOfTheWeek:
    # Check if the day is Saturday or Sunday
    if day == "Sunday" or day == "Saturday":
        print(day + " is a day off. Get some well deserved rest.")
    else:
        dayTask = lemonadeStandTasks[dayTaskIndex]
        print(day + ": " + dayTask)
        dayTaskIndex += 1
