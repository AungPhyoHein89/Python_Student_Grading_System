student_marks = {"Myanmar": 80,
                 "English": 50,
                 "Mathematics": 85,
                 "Chemistry": 42,
                 "Physics": 40,
                 "Biology": 42
                 }

final_result = "Exam Pass"

for subject, mark in student_marks.items():
  distinction_80_subjects = ["Myanmar", "English"]
  distinction_mark = 80 if subject in distinction_80_subjects else 85
  if mark >= distinction_mark:
    result = "Distinction"
  elif mark >= 40:
    result = "Pass"
  else:
    result = "Fail"
  if result == "Fail": final_result = "Exam Fail"
  print(f"{subject}: {mark} => {result}")

print("-"*30)
print(f"Overall Result: {final_result}")