"""
Title: skaggs_usersp2.py
Author: Sheldon Skaggs
Date: 7/10/2024
Description: Exercise 7.3 - Python with MongoDB, Part II
"""

# Import the MongoClient
from pymongo import MongoClient

# Import datetime object
import datetime

# Connect to my web335DB database
# PASSWORD OMITTED BEFORE COMMIT
client = MongoClient("mongodb+srv://web335_user:**********@bellevueuniversity.y1mkstf.mongodb.net/web335DB?retryWrites=true&w=majority&appName=BellevueUniversity")

# Configure a database variable
db = client['web335DB']

# Create a new user document
# Intelisense informed me that .utcnow was depreciated and to use .now(datetime.UTC)
dmcdonald = {
    "firstName": "Dave",
    "lastName": "McDonald",
    "employeeId": "1962",
    "email": "dmcdonald@me.com",
    "dateCreated": datetime.datetime.now(datetime.UTC)
}

# Insert the new user document into the database
# this will store the new document id in a variable
print("\nInsert a new user into the users collection")
dmcdonald_user_id = db.users.insert_one(dmcdonald).inserted_id

# Print the inserted id
print("\nNew user's id")
print(dmcdonald_user_id)

# Prove the above document was created
print("\nProve the new user was inserted by finding and printing their information")
print(db.users.find_one({"employeeId": "1962"}))

# Update the email address of the new document
print("\nUpdate the new user's email address")
db.users.update_one(
    {"employeeId": "1962"},
    {
        "$set": {
            "email": "dave.mcdonald@me.com"
        }
    }
)

#Prove the document was updated
print("\nProve the new user's email address was updated by finding and printing their information")
print(db.users.find_one({"employeeId": "1962"}))

# Delete the new document
print("\nDelete the new user, and print the result")
result = db.users.delete_one({"employeeId": "1962"})
print(result)

# Prove it was deleted
print("\nProve the new user was deleted by attempting to find and print their information")
print(db.users.find_one({"employeeId": "1962"}))
