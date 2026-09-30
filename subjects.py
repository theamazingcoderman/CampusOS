subject1={"Name": "Problem Solving and Python", "Code":"CSE1021", "Faculty": "Pradeep Kumar Mishra", "Credits":4}
subject2={"Name": "Calculus", "Code": "MAT1003", "Faculty": "Ezhilarasan", "Credits": 4}
subject3={"Name": "ETC", "Code": "ENG1004", "Faculty": "Anita Yadav", "Credits": 2}
subject4={"Name": "Environmental Sustainability", "Code": "CHY1006", "Faculty": "Himanshi Harish Sharma", "Credits": 2}

subjects=[subject1, subject2, subject3, subject4]

def subjects_menu():
 
 print("==========SUBJECTS==========")

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