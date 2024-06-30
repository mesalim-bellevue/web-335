// 1.A - Add a new user
newUser = {
    "firstName": "Franz",
    "lastName": "Schubert",
    "employeeId": "1013",
    "email": "fschubert@me.com",
    "dateCreated": new Date()
}

db.users.insertOne(newUser)

// 1.B - Verify the new user was added successfully
db.users.find({"email": "fschubert@me.com"}).pretty()

// 2.A - Update Mozart's email address
db.users.updateOne(
    {"lastName": "Mozart"},
    {$set: {"email": "mozart@me.com"}}
)

// 2.B - Verify the document was updated successfully
db.users.find({"lastName": "Mozart"}).pretty()

// 3 - Display all users with specific fields
db.users.find({}, {"firstName": 1, "lastName": 1, "email": 1, "_id": 0}).pretty()