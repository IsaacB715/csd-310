from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.vppafvn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
students = db.get_collection("students")

student = students.find_one({"student_id": "1007"})
print("Student ID: " + student["student_id"])
print("First Name: " + student["first_name"])
print("Last Name: " + student["last_name"])
student = students.find_one({"student_id": "1008"})
print("\nStudent ID: " + student["student_id"])
print("First Name: " + student["first_name"])
print("Last Name: " + student["last_name"])
student = students.find_one({"student_id": "1009"})
print("\nStudent ID: " + student["student_id"])
print("First Name: " + student["first_name"])
print("Last Name: " + student["last_name"])
