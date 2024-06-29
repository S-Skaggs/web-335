/*
	Title: executing_mongDB_queries.js
    Author: Sheldon Skaggs
    Date: 6/28/2024
    Description: MongoDB Shell Scripts from week 5.
 */

// Make sure we do not have a Benjamin Britten user
db.users.findOne({firstName: 'Benjamin', lastName: 'Britten'});

// Create a new user document
newUser = {firstName: 'Benjamin', lastName: 'Britten', employeeId: 'BB49', email: 'bb_classical@supermail.com', dateCreated: new Date()};

// Insert the new Benjamin Britten user
db.users.insertOne(newUser);

// Verify the new Benjamin Britten user
db.users.findOne({firstName: 'Benjamin', lastName: 'Britten'});

// Find Mozart's email address
db.users.findOne({employeeId: '1009'}, {employeeId: 1, email: 1});

// Update Mozart's email address
db.users.updateOne({employeeId: '1009'}, {$set:{email: 'mozart@me.com'}});

// Find Mozart's email address
db.users.findOne({employeeId: '1009'}, {employeeId: 1, email: 1});

// List the firstName, lastName, and email address of all users
db.users.find({},{firstName: 1, lastName: 1, email: 1, _id: 0});