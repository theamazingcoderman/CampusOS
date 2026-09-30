def profile():
   print("=========== Student Profile ===========")
   p={"Name": input("Enter Name: "), "Registration Number": input("Enter Registration Number: "), "Branch": input("Enter Branch: ")}
   
   return p
p=profile()

subject1={"Name": "Problem Solving and Python", "Code":"CSE1021", "Faculty": "Pradeep Kumar Mishra", "Credits":4}
subject2={"Name": "Calculus", "Code": "MAT1003", "Faculty": "Ezhilarasan", "Credits": 4}
subject3={"Name": "ETC", "Code": "ENG1004", "Faculty": "Anita Yadav", "Credits": 2}
subject4={"Name": "Environmental Sustainability", "Code": "CHY1006", "Faculty": "Himanshi Harish Sharma", "Credits": 2}
subjects=[subject1, subject2, subject3, subject4]

attendance1={"Name": "Problem Solving and Python", "Code": "CSE1021"}
attendance2={"Name": "Calculus", "Code": "MAT1003"}
attendance3={"Name": "ETC", "Code": "ENG1004"}
attendance4={"Name": "Environmental Sustainability", "Code": "CHY1006"}
attendance=[attendance1, attendance2, attendance3, attendance4]

tasks=[]
grades=[]
 
def subjects_menu():
 while True:
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
   continue

def attendance_menu():
 while True:
  print("===========ATTENDANCE===========")
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
    continue
   
   attended=int(input("Classes attended?:\t"))
   print()

   if attended>conducted or attended<0:
    print("Not possible\n")
    continue

   x["Conducted"]=conducted
   x["Attended"]=attended

   atp=(attended/conducted)*100
   print("Code:", x["Code"], "\n", "Classes Conducted:", conducted, "\n", "Classes Attended:", attended, "\n", "Attendance is:", round(atp, 2), "\n")
   count=0
   if atp>=75:
    while (attended/(conducted+count+1))*100>=75:
     count+=1
    if count!=1:
     print("You can miss", count, "classes, but you shouldn't\n")
    else:
     print("You can miss", count, "class, but you shouldn't\n" )
   else:
    print("Your attendance is below 75%. This is critical.\n")
    count=0
    while ((attended+count)/(conducted+count))*100<75:
     count+=1
    print("You need to attend", count, "consecutive classes to reach the required threshold.")
    print("Take your attendance seriously.\n You will face problems with your exams if you do not take immediate action")
     
  else:
   print("Give a valid input\n")
   continue

def tasks_menu():
 while True:
  print("=======TASKS=======\n")
  print("1). View Tasks")
  print("2). Add Task")
  print("3). Mark Task complete")
  print("4). Delete Task")
  print("0). Back\n")
  ch=int(input("Select a choice:\t"))
  print()

  if ch==0:
   return
 
  elif ch==1:
   print("View Tasks\n")

   if len(tasks)==0:
    print("There are no ongoing tasks at the moment\n")
   

   else:
    for i in range(len(tasks)):
     print("S.No.:", i+1)
     print("Name:", tasks[i]["Name"])
     print("Subject:", tasks[i]["Subject"])
     print("Priority:", tasks[i]["Priority"])
     print("Status:", tasks[i]["Status"])
     print()
   

  elif ch==2:
   print("Add Task")

   name=input("Enter task name:\t")
   sub=input("Enter subject code:\t")
   pr=input("Enter priority level:\t")
   print()

   task={"Name": name, "Subject": sub, "Priority": pr, "Status": "Pending"}
   tasks.append(task)
   print("Task added successfully, visible on View Tasks page") 
  

  elif ch==3:
    print("Mark Task complete")
    m=int(input("Enter serial number of task to be marked as complete:\t"))
    if len(tasks)==0:
     print("There are no tasks, add some before completing :)")
    elif m<=0 or m>len(tasks):
     print("Invalid Serial number") 
    else:
     tasks[m-1]["Status"]="Completed"

  elif ch==4:
    l=int(input("Enter serial number of the task to be removed:\t"))
    if len(tasks)==0:
     print("There are no tasks, add and complete some before deleting :)")
    elif l<=0 or l>len(tasks):
     print("Invalid Serial number")
    else:
     del tasks[l-1]
     print("Task removed successfully")
    
  else:
    print("Invalid choice")   
    continue

def grades_menu():
 
 while True:

   print("0). Return")
   print("1). View Grades")
   print("2). Enter/Update Grades")
   print("3). Calculate CGPA")
   print("4). Remove Subject grades\n")
 
   n=int(input("Select an option:\t"))
   print()

   if n==0:
    return

   elif n==1:
     if len(grades)==0:
      print("Please add some subjects before viewing grades :)")
     else: 
      for i in grades:
       print()
       print(i["Subject"])
       print(i["Subject code"])
       print("Grade Point", i["GP"])
       print()

   elif n==2:
    print("Enter/Update Grades")

    for i in range(len(subjects)):
     print(i+1,").", subjects[i]["Name"])
    
    print("0 ). Back\n")

    m=int(input("Choose the subject:\t"))

    if m==0:
     continue

    elif m in range(1,len(subjects)+1):
       x=subjects[m-1]
       g=int(input("Enter the grade (1-10):\t"))

       while g not in range(1,11):
        g=int(input("Please enter within the range (1-10)\t"))
       
       for i in range(len(grades)):
        if grades[i]["Subject code"]==x["Code"]:
         grades[i]["GP"]=g
         break

       else:
         grade={"Subject": x["Name"], "Subject code": x["Code"], "GP":g}
         grades.append(grade)
       print("Grade entered successfully, visible in View Grades page\n")

    else:
      print("Invalid subject\n")
      continue

   elif n==3:
    print("CGPA Calculator")
    points=0
    credits=0
    if len(grades)==0 or len(subjects)==0:
     print("Check if there are any grades or subjects added before calculating CGPA")
    else:
     for i in grades:
      for j in subjects:
       if i["Subject code"]==j["Code"]:
        points+=i["GP"]*j["Credits"]
        credits+=j["Credits"]
     cgpa=points/credits   
     print("Your CGPA is:", round(cgpa,2))
     print()    

   elif n==4:
    if len(grades)==0:
     print("Add some grades before removing any :)")
     continue

    for i in range(len(subjects)):
     print(i+1,").", subjects[i]["Name"])
    
    print("0 ). Back\n")

    m=int(input("Choose the subject grade to be removed:\t"))

    if m==0:
     continue

    elif m in range(1, len(subjects)+1):
     x=subjects[m-1]

     for i in range(len(grades)):
      if grades[i]["Subject code"]==x["Code"]:
       del grades[i]
       print("Grade removed successfully\n")
       break

    else:
     print("Invalid subject\n")
     continue
     
     
      


     



   else:
    print("Invalid selection\n")
    continue  

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
   print("Invalid choice")
   continue