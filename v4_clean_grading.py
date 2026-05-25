student_marks = {"Myanmar": 40,
                 "English": 41,
                 "Mathematic": 85,
                 "Chemistry": 62,
                 "Physics": 40,
                 "Biology": 34
                 }

def get_subject_status(subject,mark):
  distinction_80_subjects = ["Myanmar", "English"]
  distinction_mark = 80 if subject in distinction_80_subjects else 85
  if mark >= distinction_mark:
    return "Distinction"
  elif mark >= 40:
    return "Pass"
  else:
    return "Fail"

all_passed = True
total_marks = 0

for subject, mark in student_marks.items():
  result = get_subject_status(subject, mark)
  total_marks += mark

  if result == "Fail":
    all_passed = False

  print(f"{subject}: {mark} => {result}")

final_result = "Pass" if all_passed else "Fail"
average_marks = total_marks/len(student_marks)

print("-"*30)
print(f"Overall Result:{final_result}")
print(f"Total Marks   :{total_marks}")
print(f"Average Marks :{average_marks:.2f}")