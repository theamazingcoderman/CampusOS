# CampusOS

### Your Personalized VTOP

CampusOS is a Python-based command-line student management system designed to bring commonly used academic and productivity features into one place.

It allows students to manage their profile, view subject information, monitor attendance, track academic tasks, manage grades, calculate CGPA, and view an overall dashboard.

## Features

### 1. Dashboard
Provides a quick overview of:
- Student name
- Number of subjects
- Number of tasks
- Pending tasks
- Completed tasks
- Task completion progress
- Number of entered grades

### 2. Subjects
Displays:
- Subject name
- Subject code
- Faculty
- Credits

### 3. Attendance
Allows the user to enter:
- Classes conducted
- Classes attended

The system calculates the attendance percentage and provides guidance based on the 75% attendance threshold.

### 4. Tasks
Allows students to:
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks

Each task contains a name, subject code, priority, and status.

### 5. Grades and CGPA
Allows students to:
- Enter grade points
- Update grade points
- View entered grades
- Remove grades
- Calculate CGPA using subject credits

### 6. Profile
Stores and displays the student's:
- Name
- Registration Number
- Branch

## Technologies Used

- Python
- Python functions
- Conditional statements
- Loops
- Lists
- Dictionaries
- Modules
- Basic data processing

## Project Structure

```text
CampusOS/
|--> main.py
|--> tudent_profile.py
|--> subjects.py
|--> attendance.py
|--> tasks.py
|--> grades.py
|--> dashboard.py
|--> README.md
|--> statement.md

MODULE DESCRIPTION:

1. main.py
---> Controls the main CampusOS menu and program flow

2. student_profile.py
---> Handles student profile information

3. subjects.py
---> Stores subject information and provides the subjects menu

4. attendance.py
---> Handles attendance input and calculations

5. tasks.py
---> Handles task management

6. grades.py
---> Handles grades and CGPA calculation

7. dashboard.py
---> Displays the student's academic overview

HOW TO RUN:
Requirements:

*Python 3.x installed on the system.

Steps:
1. Clone or download the repository.
2. Open a terminal in the CampusOS project directory.
3. Run:
   python main.py
4. Follow the instructions displayed in the terminal

DATA HANDLING:

The current version of CampusOS stores data in memory while the program is running.

Therefore, information entered during one session is not permanently stored after the program exits.

Persistent storage is planned as a future enhancement.

TESTING

The major functional modules have been tested during development, including:

1. Profile creation and display
2. Subject viewing
3. Attendance calculations
4. Attendance validation
5. Task creation
6. Task completion
7. Task deletion
8. Grade entry and updating
9. Grade validation
10. CGPA calculation
11. Grade deletion
12. Dashboard statistics
13. Navigation between menus

FUTURE ENHANCEMENTS:

Possible future versions of CampusOS may include:

1. Persistent data storage
2. Graphical User Interface
3. Database integration
4. More detailed academic analytics
5. Timetable management
6. Assignment and deadline reminders
7. Semester-wise academic records
8. Attendance history and visualization

AUTHOR
Naman Chowdhary