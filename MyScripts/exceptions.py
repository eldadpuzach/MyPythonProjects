student = {
    "name": "Mark",
 #   "last_name": "Spencer",
    "student_id": 15163,
    "feedback": None
}

try:
    last_name = student["last_name"]
#    print("Student's last name is: " + last_name)
except KeyError:
    print("Error in finding last_name")

print('This code executes!')