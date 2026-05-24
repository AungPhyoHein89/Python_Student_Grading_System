# Save the mark list of a student
student_marks = {"Myanmar": 40,
                 "English": 60,
                 "Mathematic": 85,
                 "Chemistry": 75,
                 "Physics": 85,
                 "Biology": 75
                 }

# Separate subject and mark using .item() method
for subject, mark in student_marks.items():
  status = "Fail" if mark < 40 else "Pass"
  print(f"{subject}: {mark} -> {status}")