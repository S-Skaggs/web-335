"""
Title: skaggs_usersp1.py
Author: Sheldon Skaggs
Date: 7/6/2024
Description: Excercise 6.3 - Python with MongoDB, Part I
"""

# Import the MongoClient
from pymongo import MongoClient

# Create a connection string to connect to the database
# PLEASE NOTE, PASSWORD OMITTED BEFORE COMMIT
client = MongoClient("mongodb+srv://web335_user:************@bellevueuniversity.y1mkstf.mongodb.net/web335DB?retryWrites=true&w=majority&appName=BellevueUniversity")

# Configure a variable to access the web335DB Database
db = client["web335DB"]

# Print the client to test correct setup
print("\nDisplay the client, we should not see an error.")
print(client)

# Display all documents in the users collection with the find() function
print("\nDisplay all documents in the users collection")
for user in db.users.find():
    print(user)

# Display the document in the users collection with employeeId of 1011 with the findOne function AKA find_one
print("\nFind user with employeeId 1011")
print(db.users.find_one({"employeeId": "1011"}))

# Display the document in the users collection with a last name of Mozart
# This potentially could be more than one document so I will use find()
print("\nFind users with last name of Mozart")
for user in db.users.find({"lastName": "Mozart"}):
    print(user)