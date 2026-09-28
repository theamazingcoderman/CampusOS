def profile():
   print("=========== Student Profile ===========")
   p={"Name": input("Enter Name: "), "Registration Number": input("Enter Registration Number: "), "Branch": input("Enter Branch: ")}
   
   return p
p=profile()

subject1={"Name": "Problem Solving and Python", "Code":"CSE1021", "Faculty": "Pradeep Kumar Mishra", "Credits":4}
subject2={"Name": "Calculus", "Code": "MAT1003", "Faculty": "Unknown", "Credits": 4}
subject3={"Name": "ETC", "Code": "ENG1004", "Faculty": "Anita Yadav", "Credits": 2}
subject4={"Name": "Environmental Sustainability", "Code": "CHY1006", "Faculty": "Himanshi Harish Sharma", "Credits": 2}
subjects=[subject1, subject2, subject3, subject4]

attendance1={"Name": "Problem Solving and Python", "Code": "CSE1021", "Classes Conducted": 34, "Classes Attended": 32}
attendance2={"Name": "Calculus", "Code": "MAT1003", "Classes Conducted": 35, "Classes Attended": 34}
attendance3={"Name": "ETC", "Code": "ENG1004", "Classes Conducted": 12, "Classes Attended": 10}
attendance4={"Name": "Environmental Sustainability", "Code": "CHY1006", "Classes Conducted": 34, "Classes Attended": 27}
attendance=[attendance1, attendance2, attendance3, attendance4]

def subjects_menu():
 print(0,").", "Back")
 for i in range(len(subjects)):
    x=subjects[i]
    print(i+1,").", x["Name"])
    print()
 n=int(input("Choose subject:\t"))
 print()
 if n==0:
  return
 elif n in range(1,len(subjects)+1):
  x=subjects[n-1]
  print("Code:", x["Code"], "\n" "Faculty:", x["Faculty"], "\n" "Credits:", x["Credits"], "\n")
 else:
  print("Give valid input\n")
  return

def attendance_menu():
 print(0,").", "Back\n")
 for i in range(len(attendance)):
    x=attendance[i]
    print(i+1,").", x["Name"])
    print()
 n=int(input("Choose subject:\t"))
 print()
 if n==0:
  return
 elif n in range(1,len(attendance)+1):
  x=attendance[n-1]
  atp=(x["Classes Attended"]/x["Classes Conducted"])*100
  print("Code:", x["Code"], "\n", "Classes Conducted:", x["Classes Conducted"], "\n", "Classes Attended:", x["Classes Attended"], "\n", "Attendance is:", round(atp, 2), "\n")
 else:
  print("Give a valid input\n")
  return

while True:
  print("CampusOS")
  print("Your personalized VTOP")
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
   print("==========Dashboard========\n")
     
  elif ch==2: 
   subjects_menu()
   
  elif ch==3:
   attendance_menu()
  
  elif ch==4:
   print("Task module in progress")
  
  elif ch==5:
   print("Grades and CGPA module in progress")
  
  elif ch==6:
   print("Name: ",p["Name"])
   print("Registration Number: ",p["Registration Number"])
   print("Branch: ",p["Branch"],"\n")
  
  
  elif ch==0:
   print("Thank you for choosing CampusOS, your personalised VTOP")
   break

  else:
   print("Invalid choice")






