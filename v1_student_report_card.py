student_1 = {"Name": "Aung Aung",
             "Class": "Grade 11",
             "marks": {"Myanmar": 40, "English": 39, "Math": 62}
             }

student_2 = {"Name": "Su Su",
             "Class": "Grade 12",
             "marks": {"Myanmar": 80, "English": 85, "Math": 90}
             }

def generate_report_card(student):
  print("-"*30)
  print(f"Name: {student['Name']}")
  print(f"Class: {student['Class']}")
  
  for subject, mark in student["marks"].items():
    subject_status = "Fail" if mark < 40 else "Pass"
    print(f"{subject}: {mark} => {subject_status}")  
  print("-"*30)

generate_report_card(student_1)
generate_report_card(student_2)