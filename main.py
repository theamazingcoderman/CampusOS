from student_profile import profile
from subjects import subjects, subjects_menu
from attendance import attendance, attendance_menu
from tasks import tasks, tasks_menu
from grades import grades, grades_menu
from dashboard import dashboard

p=profile()

while True:
  print("CampusOS")
  print("Your personalised VTOP")
  print("1. Dashboard")
  print("2. Subjects")
  print("3. Attendance")
  print("4. Tasks")
  print("5. Grades and CGPA")
  print("6. Profile")
  print("0. Exit \n") 

  ch=int(input("What do you want to see?:\t"))
  print()

  if ch==1:
   dashboard(p, subjects, tasks, grades)
   
  elif ch==2: 
     subjects_menu()
   
  elif ch==3:
    attendance_menu()
  
  elif ch==4:
    tasks_menu()
  
  elif ch==5:
    grades_menu()
  
  elif ch==6:
    print("Name: ",p["Name"])
    print("Registration Number: ",p["Registration Number"])
    print("Branch: ",p["Branch"],"\n")
  
  elif ch==0:
    print("Thank you for choosing CampusOS, your personalised VTOP\n")
    break

  else:
    print("Invalid choice\n")
    continue