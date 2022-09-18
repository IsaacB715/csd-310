from pymongo import MongoClient

def display_student(student):
    print("Student ID: ", student["student_id"])
    print("First Name: ", student["first_name"])
    print("Last Name: ", student["last_name"])
    print()

url = "mongodb+srv://admin:admin@cluster0.vppafvn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
students = db.get_collection("students")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find(): 
    display_student(student)
print()
print("-- INSERT STATEMENTS --")

fred = {"first_name": "Emily","last_name": "White", "student_id": "1010"}
 
id = students.insert_one(fred).inserted_id

print("Inserted student record into the students collection with document_id ", id)
print()
print("-- DISPLAYING STUDENT TEST DOC --")
student = students.find_one({"student_id": "1010"})
display_student(student)
students.delete_one({"student_id": "1010"})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find(): 
    display_student(student)
