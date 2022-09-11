from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.vppafvn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
students = db.get_collection("students")
fred = {"first_name": "John","last_name": "Doe", "student_id": "1007"}
 
student_id = students.insert_one(fred).inserted_id
print("Inserted student record John Doe into the students collection with document id" + student_id)
fred = {"first_name": "Sarah","last_name": "Smith", "student_id": "1008"}
 
student_id = students.insert_one(fred).inserted_id
print("Inserted student record Sarah Smith into the students collection with document id" + student_id)
fred = {"first_name": "Will","last_name": "Frank", "student_id": "1009"}
 
student_id = students.insert_one(fred).inserted_id
print("Inserted student record Will Frank into the students collection with document id" + student_id)
