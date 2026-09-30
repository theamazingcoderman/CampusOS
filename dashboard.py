def dashboard(p, subjects, tasks, grades):
    print("==========Dashboard========")
    print("Welcome, Master", p["Name"])
    print("Subjects:", len(subjects))
    print("Tasks:", len(tasks))

    pending=0
    completed=0

    for i in tasks:
     if i["Status"]=="Pending":
      pending+=1

     elif i["Status"]=="Completed":
      completed+=1
 
    print("Pending Tasks:", pending)
    print("Completed Tasks:", completed) 

    if len(tasks)==0:
     print("Task Progress: 0%")

    else:
     tp=((completed/len(tasks))*100)
     print("Task Progress:", round(tp,2), "%")

    print("Grades entered:", len(grades))
    print()