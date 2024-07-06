// Author: Meher Salim
// Date: 07/06/2024
// File Name: salim-assignment6.2.js
// Description: Perform various operations on the houses and student’s collections using MongoDB Shell.

// 2.a
// Display all students
db.students.find().pretty()

// 2.b
// Add a new student
newStudent = {
    "firstName": "Severus",
    "lastName": "Snape",
    "studentId": "s1019",
    "houseId": "h1010",
    "dateCreated": new Date()
}

db.students.insertOne(newStudent)

// Verify the new student was added successfully
db.students.find({"firstName": "Severus", "lastName": "Snape"}).pretty()

// 2.c
// Update the year of the student added in step b
db.students.updateOne(
    {"firstName": "Severus", "lastName": "Snape"},
    {$set: {"year": 7}}
)

// Verify the property was updated successfully
db.students.find({"firstName": "Severus", "lastName": "Snape"}).pretty()

// 2.d
// Delete the student created in step b
db.students.deleteOne({"firstName": "Severus", "lastName": "Snape"})

// Verify the student was removed successfully
db.students.find({"firstName": "Severus", "lastName": "Snape"}).pretty()

// 2.e
// Display all students by house
db.students.aggregate([
    { $group: { _id: "$houseId", students: { $push: "$$ROOT" } } },
    { $lookup: { from: "houses", localField: "_id", foreignField: "houseId", as: "houseDetails" } },
    { $unwind: "$houseDetails" },
    { $sort: { "houseDetails.houseId": 1 } }
]).forEach(house => {
    print(house.houseDetails.houseId + " - " + house.houseDetails.mascot)
    house.students.forEach(student => {
        printjson(student)
    })
})

// 2.f
// Display all students in house Gryffindor
gryffindorStudents = db.students.find({"houseId": "h1007"}).pretty()
print("Gryffindor")
gryffindorStudents.forEach(student => {
    printjson(student)
})

// 2.g
// Display all students in the house with an Eagle mascot
eagleHouseId = db.houses.findOne({"mascot": "Eagle"}).houseId
eagleHouseStudents = db.students.find({"houseId": eagleHouseId}).pretty()
print("Eagle House")
eagleHouseStudents.forEach(student => {
    printjson(student)
})