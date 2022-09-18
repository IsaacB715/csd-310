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
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
student = students.find_one({"student_id": "1007"})
display_student(student)
