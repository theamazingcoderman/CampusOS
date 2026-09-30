tasks=[]
def tasks_menu():
 
 while True:

  print("=======TASKS=======")

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
   print("Task added successfully, visible on View Tasks page\n") 
  
  elif ch==3:
    print("Mark Task Complete")
    m=int(input("Enter serial number of task to be marked as complete:\t"))

    if len(tasks)==0:
     print("There are no tasks, add some before completing :)\n")

    elif m<=0 or m>len(tasks):
     print("Invalid Serial number\n") 

    else:
     tasks[m-1]["Status"]="Completed"
     print("Task marked as complete, congrats!")

  elif ch==4:
    l=int(input("Enter serial number of the task to be removed:\t"))

    if len(tasks)==0:
     print("There are no tasks, add and complete some before deleting :)\n")

    elif l<=0 or l>len(tasks):
     print("Invalid Serial number\n")

    else:
     del tasks[l-1]
     print("Task removed successfully\n")
    
  else:
    print("Invalid choice\n")   
    continue