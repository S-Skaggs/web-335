/*
	Title: executing_mongDB_queries.js
    Author: Sheldon Skaggs
    Date: 6/20/2024
    Description: MongoDB Shell Scripts from Guide 3: Executing MongoDB Queries.
 */

// Find the user Claude
db.users.findOne({firstName: 'Claude'});

// Find all users
db.users.find();

// Create a user document
user = {firstName: 'Bryce', lastName: 'Wane', employeeId: 'BW123', email: 'bryce.wane@supermail.com', dateCreated: new Date()};

// Add the new user document
db.users.insertOne(user);

// Find the new user by firstName
db.users.findOne({firstName: 'Bryce'});

// Find the new user by firstName and lastName
db.users.findOne({firstName: 'Bryce', lastName: 'Wane'});

// Update the enw user's email
db.users.updateOne({employeeId: 'BW123'}, {$set: {email: 'bryce.isnotbatman@supermail.com'}});

// Verify new user was updated by finding them by employeeId
db.users.findOne({employeeId: 'BW123'});

// Find user with projections
db.users.findOne({employeeId: 'BW123'}, {firstName: 1, email: 1});

// Find user with projections without the _id
db.users.findOne({employeeId: 'BW123'}, {_id: 0, firstName: 1, lastName: 1, email: 1});

// Delete the new user
db.users.deleteOne({employeeId: 'BW123'});

// Verify new user has been deleted
db.users.findOne({employeeId: 'BW123'});