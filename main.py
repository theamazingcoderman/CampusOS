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

attendance1={"Name": "Problem Solving and Python", "Code": "CSE1021"}
attendance2={"Name": "Calculus", "Code": "MAT1003"}
attendance3={"Name": "ETC", "Code": "ENG1004"}
attendance4={"Name": "Environmental Sustainability", "Code": "CHY1006"}
attendance=[attendance1, attendance2, attendance3, attendance4]

def subjects_menu():
 print(0,").", "Back")
 for i in range(len(subjects)):
    x=subjects[i]
    print(i+1,").", x["Name"])
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
 print(0,").", "Back")
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
  conducted=int(input("Classes conducted?:\t"))
  if conducted<=0:
   print("Not possible")
   return
  attended=int(input("Classes attended?:\t"))
  if attended>conducted or attended<0:
   print("Not possible")
   return
  atp=(attended/conducted)*100
  print("Code:", x["Code"], "\n", "Classes Conducted:", conducted, "\n", "Classes Attended:", attended, "\n", "Attendance is:", round(atp, 2), "\n")
  count=0
  if atp>=75:
   while (attended/(conducted+count+1))*100>=75:
    count+=1
   if count!=1:
    print("You can miss", count, "classes")
   else:
    print("You can miss", count, "class" )
  else:
   print("Your attendance is below 75%. This is critical.")
   count=0
   while ((attended+count)/(conducted+count))*100<75:
    count+=1
   print("You need to attend", count, " consecutive classes to reach the required threshold")
   print("Take your attendance seriously, you will face problems with your exams if you do not take immediate action")
     
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
   print("Thank you for choosing CampusOS, your personalised VTOP\n")
   break

  else:
   print("Invalid choice")