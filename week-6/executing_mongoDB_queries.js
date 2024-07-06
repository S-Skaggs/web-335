/*
  Title: executing_mongDB_queries.js
  Author: Sheldon Skaggs
  Date: 7/6/2024
  Description: MongoDB Shell Scripts from week 6.
*/

// After using CD to get to the directory of my houses.js script I connected to
// my MongoDB and loaded the script using this query
load("houses.js");

// Display all students using find()
db.students.find();

// Create a newStudent document to be added
newStudent = {
  firstName: 'Alastair',
  lastName: 'Finch',
  studentId: 'sl101',
  houseId: 'hl009'
}

// Add the new student to the students collection
db.students.insertOne(newStudent);

// Prove the new student was added by using findOne()
db.students.findOne({studentId: 'sl101'});

// Update the new student's lastName
db.students.updateOne({studentId: 'sl101'}, {lastName: 'Goldfinch'});

// Prove lastName was updated by using findOne
db.students.findOne({studentId: 'sl101'});

// Delete the new student using deleteOne
db.students.deleteOne({studentId: 'sl101'});

// Prove the new student was deleted using findOne
db.students.findOne({studentId: 'sl101'});

// Display all students by house with an aggregate query
// I used houses as my base since the desired order is houses -> students
db.houses.aggregate([{$lookup:{from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_docs'}}]);

// Display all students in house Gryffindor
// I used houses as my base since the desired order is house -> students
// I used the $match to ensure we obtained the proper house based on the houseId
db.houses.aggregate([{$match:{'houseId': 'h1007'}}, {$lookup:{from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_docs'}}]);

// Display all students in houses with an Eagle mascot
// I used houses as my base since the desired order is houses -> students
// I used the $match to ensure we obtained houses that had Eagle as the mascot
db.houses.aggregate([{$match:{mascot: 'Eagle'}}, {$lookup:{from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'student_docs'}}]);
