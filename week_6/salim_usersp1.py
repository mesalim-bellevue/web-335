"""
Title: salim_usersp1.py
Author: Meher Salim
Date: 07/06/2024
Description: Build a Python program that connects to your MongoDB database and performs various operations.
"""

from pymongo import MongoClient

# Replace <your_connection_string> with your actual connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Connect to the web335DB database
db = client['web335DB']

# Display all documents in the user's collection
print("All users:")
for user in db.users.find():
    print(user)

# Display the document where the employeeId is 1011
employee_id_doc = db.users.find_one({"employeeId": "1011"})
print("\nDocument with employeeId 1011:")
print(employee_id_doc)

# Display the document where the lastName is Mozart
last_name_doc = db.users.find_one({"lastName": "Mozart"})
print("\nDocument with lastName Mozart:")
print(last_name_doc)
