attendance1={"Name": "Problem Solving and Python", "Code": "CSE1021"}
attendance2={"Name": "Calculus", "Code": "MAT1003"}
attendance3={"Name": "ETC", "Code": "ENG1004"}
attendance4={"Name": "Environmental Sustainability", "Code": "CHY1006"}

attendance=[attendance1, attendance2, attendance3, attendance4]

def attendance_menu():
 
 while True:

  print("===========ATTENDANCE===========")

  for i in range(len(attendance)):
    x=attendance[i]
    print(i+1,").", x["Name"])

  print(0,").", "Back")
  print()
  n=int(input("Choose subject:\t"))
  print()

  if n==0:
   return
  
  elif n in range(1,len(attendance)+1):
   x=attendance[n-1]
   conducted=int(input("Classes conducted?:\t"))

   if conducted<=0:
    print("Not possible\n")
    continue
   
   attended=int(input("Classes attended?:\t"))
   print()

   if attended>conducted or attended<0:
    print("Not possible\n")
    continue

   x["Conducted"]=conducted
   x["Attended"]=attended

   atp=(attended/conducted)*100
   print("Code:", x["Code"], "\n", 
         "Classes Conducted:", conducted, "\n", 
         "Classes Attended:", attended, "\n", 
         "Attendance is:", round(atp, 2), 
         "\n")
   
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
    print("You need to attend", count, 
          "consecutive classes to reach the required threshold.")
    print("Take your attendance seriously.\n" \
    "You will face problems with your exams if you do not take immediate action.")
    print()
     
  else:
   print("Give a valid input\n")
   continue