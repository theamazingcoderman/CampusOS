# CampusOS - Testing Documentation

## 1. Introduction

CampusOS was tested during development to verify the functionality of its major modules and to ensure that the different menu operations work correctly.

The testing covered normal inputs, invalid inputs, calculations, navigation, and interactions between different modules.

---

## 2. Profile Testing

### Test Case 1 - Profile Creation

Action:
Enter the student's name, registration number, and branch.

Expected Result:
The system should accept the details and start CampusOS.

Actual Result:
The profile was created successfully and the main menu was displayed.

Status:
PASS

---

## 3. Dashboard Testing

### Test Case 2 - Empty Dashboard

Action:
Open the Dashboard before adding any tasks.

Expected Result:
The Dashboard should display the number of subjects and tasks, with task progress shown as 0%.

Actual Result:
The Dashboard displayed the correct subject count, task count, and 0% task progress.

Status:
PASS


### Test Case 3 - Dashboard With Tasks and Grades

Action:
Add tasks, complete a task, and enter grades. Then open the Dashboard.

Expected Result:
The Dashboard should display the correct number of subjects, tasks, pending tasks, completed tasks, task progress, and entered grades.

Actual Result:
The Dashboard displayed the correct values.

Status:
PASS

---

## 4. Subject Testing

### Test Case 4 - View Subjects

Action:
Open the Subjects module and select a subject.

Expected Result:
The system should display the subject code, faculty, and credits.

Actual Result:
The selected subject information was displayed correctly.

Status:
PASS


### Test Case 5 - Subject Navigation

Action:
Use the Back option in the Subjects module.

Expected Result:
The system should return to the appropriate menu.

Actual Result:
The system returned to the main menu correctly.

Status:
PASS

---

## 5. Attendance Testing

### Test Case 6 - Attendance Above 75%

Input:

Classes Conducted: 40

Classes Attended: 32

Expected Result:
The system should calculate the attendance as 80% and determine the number of classes that can be missed while maintaining the 75% threshold.

Actual Result:
The system calculated 80% attendance and displayed that 2 classes could be missed.

Status:
PASS


### Test Case 7 - Attendance Below 75%

Input:

Classes Conducted: 40

Classes Attended: 20

Expected Result:
The system should identify that the attendance is below 75% and calculate the number of consecutive classes required to reach the threshold.

Actual Result:
The system identified the attendance as critical and calculated the required consecutive classes correctly.

Status:
PASS


### Test Case 8 - Invalid Classes Conducted

Input:

Classes Conducted: 0

Expected Result:
The system should reject the input.

Actual Result:
The system rejected the input and displayed an appropriate message.

Status:
PASS


### Test Case 9 - Invalid Classes Attended

Input:

Classes Conducted: 40

Classes Attended: 45

Expected Result:
The system should reject the input because attended classes cannot be greater than conducted classes.

Actual Result:
The system rejected the input.

Status:
PASS

---

## 6. Task Testing

### Test Case 10 - Add Task

Action:
Enter a task name, subject code, and priority.

Expected Result:
The task should be added with a Pending status.

Actual Result:
The task was added successfully.

Status:
PASS


### Test Case 11 - View Tasks

Action:
Open View Tasks after adding tasks.

Expected Result:
The system should display the task name, subject, priority, and status.

Actual Result:
All task details were displayed correctly.

Status:
PASS


### Test Case 12 - Complete Task

Action:
Select a task and mark it as completed.

Expected Result:
The task status should change from Pending to Completed.

Actual Result:
The task was marked as Completed successfully.

Status:
PASS


### Test Case 13 - Delete Task

Action:
Select a task and delete it.

Expected Result:
The selected task should be removed from the task list.

Actual Result:
The task was removed successfully.

Status:
PASS

---

## 7. Grade and CGPA Testing

### Test Case 14 - View Grades With No Grades

Action:
Open View Grades before entering any grades.

Expected Result:
The system should inform the user that grades need to be added.

Actual Result:
The system displayed the appropriate message.

Status:
PASS


### Test Case 15 - Enter Grade

Action:
Enter a grade point for a subject.

Expected Result:
The grade point should be added and should appear in View Grades.

Actual Result:
The grade point was entered successfully and appeared in View Grades.

Status:
PASS


### Test Case 16 - Update Grade

Action:
Enter a different grade point for a subject that already has a grade.

Expected Result:
The existing grade point should be updated instead of creating a duplicate entry.

Actual Result:
The grade point was updated successfully.

Status:
PASS


### Test Case 17 - Invalid Grade

Input:

Grade Point: 11

Expected Result:
The system should reject the value and request a grade point between 1 and 10.

Actual Result:
The system rejected the invalid value and requested a valid grade point.

Status:
PASS


### Test Case 18 - CGPA Calculation

Action:
Enter grade points for subjects and select Calculate CGPA.

Expected Result:
The system should calculate CGPA using grade points and subject credits.

Actual Result:
The CGPA was calculated successfully.

Status:
PASS


### Test Case 19 - Remove Grade

Action:
Select a subject grade and remove it.

Expected Result:
The selected grade should be removed from the grade list.

Actual Result:
The grade point was removed successfully.

Status:
PASS


### Test Case 20 - Recalculate CGPA

Action:
Remove a grade and calculate CGPA again.

Expected Result:
The CGPA should be recalculated using the remaining entered grades.

Actual Result:
The CGPA was recalculated successfully.

Status:
PASS

---

## 8. Profile Display Testing

### Test Case 21 - View Profile

Action:
Open the Profile option from the main menu.

Expected Result:
The system should display the student's name, registration number, and branch.

Actual Result:
The profile information was displayed correctly.

Status:
PASS

---

## 9. Navigation Testing

### Test Case 22 - Main Menu Navigation

Action:
Navigate between Dashboard, Subjects, Attendance, Tasks, Grades and CGPA, and Profile.

Expected Result:
The user should be able to access the available modules and return to the main menu.

Actual Result:
Navigation between the modules worked correctly.

Status:
PASS


### Test Case 23 - Exit

Action:
Select the Exit option from the main menu.

Expected Result:
The program should terminate and display a closing message.

Actual Result:
The program exited successfully and displayed the closing message.

Status:
PASS

---

## 10. Testing Summary

The major functional modules of CampusOS were tested during development.

The testing covered:

1. Profile creation and display
2. Subject viewing
3. Subject navigation
4. Dashboard statistics
5. Attendance calculation
6. Attendance validation
7. Task creation
8. Task viewing
9. Task completion
10. Task deletion
11. Grade entry
12. Grade updating
13. Grade validation
14. CGPA calculation
15. Grade deletion
16. Profile display
17. Navigation between menus
18. Program exit

All planned functional tests were completed successfully.