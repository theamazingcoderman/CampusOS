from subjects import subjects, subjects_menu
grades=[]
def grades_menu():
 
 while True:

   print("0). Return")
   print("1). View Grades")
   print("2). Enter/Update Grades")
   print("3). Calculate CGPA")
   print("4). Remove Subject Grade\n")
 
   n=int(input("Select an option:\t"))
   print()

   if n==0:
    return

   elif n==1:
     if len(grades)==0:
      print("Please add some subjects before viewing grades :)\n")

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
       g=int(input("Enter the grade point(1-10):\t"))

       while g not in range(1,11):
        g=int(input("Please enter within the range (1-10)\t"))
       
       for i in range(len(grades)):
        if grades[i]["Subject code"]==x["Code"]:
         grades[i]["GP"]=g
         break

       else:
         grade={"Subject": x["Name"], "Subject code": x["Code"], "GP":g}
         grades.append(grade)
       print("Grade point entered successfully, visible in View Grades page\n")

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
     print("Add some grade points before removing any :)")
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
       print("Grade point removed successfully\n")
       break

    else:
     print("Invalid subject\n")
     continue
     
   else:
    print("Invalid selection\n")
    continue