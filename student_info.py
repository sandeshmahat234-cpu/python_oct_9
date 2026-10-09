student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}
print("Student information:", student)
student["marks"] += 5
student["status"] = "Pass" if student["marks"] >= 40 else "Fail"
print("Updated student information:", student)
