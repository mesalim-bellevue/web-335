/*
Designer:       Meher Salim
Date:           06/20/2024
File Name:      salim-excerise4.3.js
Description:    MongoDB queries for excerise 4.3 (MongoDB Database Setup and Querying with
MongoDB Shell)
*/

// Query a: Display all users in the collection
db.users.find().pretty();

// Query b: Display the user with the email address jbach@me.com
db.users.find({ email: 'jbach@me.com' }).pretty();

// Query c: Display the user with the last name Mozart
db.users.find({ lastName: 'Mozart' }).pretty();

// Query d: Display the user with the first name Richard
db.users.find({ firstName: 'Richard' }).pretty();

// Query e: Display the user with employeeId 1010
db.users.find({ employeeId: 1010 }).pretty();