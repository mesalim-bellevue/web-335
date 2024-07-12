"""
Title: salim_usersp2.py
Author: Meher Salim
Date: 07/12/2024
Description: Build a Python program that connects to MongoDB database and performs various CRUD operations.
"""

from pymongo import MongoClient
import datetime

# Replace <your_connection_string> with your actual connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")
# Connect to the web335DB database
db = client['web335DB']

# Create a new user document
new_user = {
    "firstName": "Taylor",
    "lastName": "Swift",
    "employeeId": "1014",
    "email": "tswift@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
result = db.users.insert_one(new_user)
print(f"Inserted new user with ID: {result.inserted_id}")

# Prove the insert worked by searching the collection for the document
print("Document created:")
print(db.users.find_one({"employeeId": "1014"}))

# Update the email address of the document
update_result = db.users.update_one(
    {"employeeId": "1014"},
    {"$set": {"email": "taylor.swift@me.com"}}
)

# Check if update was acknowledged and print updated document
if update_result.modified_count > 0:
    print("Document updated:")
    print(db.users.find_one({"employeeId": "1014"}))
else:
    print("Document update failed.")

# Delete the document that was created
delete_result = db.users.delete_one({"employeeId": "1014"})

# Check if deletion was acknowledged and print result
if delete_result.deleted_count > 0:
    print("Document deleted successfully.")
else:
    print("Document deletion failed.")

# Prove the delete worked by searching for the deleted document
print("After deletion, searching for employeeId 1014:")
print(db.users.find_one({"employeeId": "1014"}))
