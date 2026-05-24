# Saving subject and mark data in dictionary
student_marks = {"Myanmar": 80,
           "English": 80,
           "Mathematic": 85,
           "Physics": 84,
           "Chemistry": 90,
           "Biology": 39
          }

# pass/fail/distinction
for subject, mark in student_marks.items():
  if subject in ["Myanmar", "English"]:
    if mark >= 80:
      status = "Distinction"
    elif mark >= 40:
      status = "Pass"
    else:
      status = "Fail"
  else:
    if mark >= 85:
      status = "Distinction"
    elif mark >= 40:
      status = "Pass"
    else:
      status = "Fail"
  print(f"{subject}: {mark} -> {status}")