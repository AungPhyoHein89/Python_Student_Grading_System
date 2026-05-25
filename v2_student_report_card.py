student_1 = {"Name": "Aung Aung",
             "Class": "Grade 11",
             "marks": {"Myanmar": 40, "English": 80, 
                       "Math": 85, "Chemistry": 42,
                       "Physics": 62, "Biology": 39}
             }

student_2 = {"Name": "Su Su",
             "Class": "Grade 12",
             "marks": {"Myanmar": 80, "English": 85,
                       "Math": 90, "Chemistry": 42,
                       "Physics": 62, "Biology": 90}
             }

def generate_report_card(student):
  exam_result = True
  print("-"*30)
  print(f"Name: {student['Name']}")
  print(f"Class: {student['Class']}")
  print("\n....Exam Results....")
  for subject, mark in student['marks'].items():
    distinction_80_marks = ["Myanmar", "English"]
    distinction_mark = 80 if subject in distinction_80_marks else 85
    if mark >= distinction_mark:
      subject_status = "Distinction"
    elif mark >= 40:
      subject_status ="Pass"
    else:
      subject_status = "Fail"
      exam_result = False
  
    print(f"{subject}: {mark} => {subject_status}")
  
  overall_result = "Exam Pass" if exam_result else "Exam Fail"
    
  print(f"\nFinal Result: {overall_result}")
  print("-"*30)

  
generate_report_card(student_1)

generate_report_card(student_2)