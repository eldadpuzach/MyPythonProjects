student = {
    "name": "Mark",
 #   "last_name": "Spencer",
    "student_id": 15163,
    "feedback": None
}
student["last_name"] = "Spencer"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
#    print("Student's last name is: " + last_name)
except KeyError:
    print("Error in finding last_name")
except TypeError:
    print("I can't add together this two Character types")

print('This code executes!')