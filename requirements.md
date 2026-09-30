# CampusOS - Requirements

## 1. Functional Requirements

### FR1 - Student Profile
The system shall allow the user to enter and view their name, registration number, and branch.

### FR2 - Subject Management
The system shall display the available subjects along with their subject codes, faculty names, and credits.

### FR3 - Attendance Management
The system shall allow the user to enter classes conducted and classes attended for a subject.

The system shall calculate the attendance percentage and provide information about the number of classes that can be missed or the number of consecutive classes required to reach the 75% threshold.

The system shall reject invalid attendance values.

### FR4 - Task Management
The system shall allow the user to:
- Add a task
- View tasks
- Mark a task as completed
- Delete a task

Each task shall contain a task name, subject code, priority, and status.

### FR5 - Grade Management
The system shall allow the user to:
- Enter grade points
- Update grade points
- View grade points
- Remove grade points

The system shall validate grade points to ensure that they remain within the range of 1 to 10.

### FR6 - CGPA Calculation
The system shall calculate CGPA using grade points and the corresponding subject credits.

### FR7 - Dashboard
The system shall display a summary of the student's subjects, tasks, task status, task completion percentage, and entered grades.

### FR8 - Navigation
The system shall allow the user to navigate between different modules and return to the main menu.

---

## 2. Non-Functional Requirements

### NFR1 - Usability
The system should provide a simple command-line interface with clearly labelled menus and instructions.

### NFR2 - Reliability
The system should produce consistent calculations for attendance and CGPA based on the entered values.

### NFR3 - Maintainability
The system shall be divided into separate Python modules, with each module handling a specific responsibility.

### NFR4 - Error Handling
The system should validate important user inputs and reject invalid values such as impossible attendance values and grade points outside the 1-10 range.

### NFR5 - Performance
The system should perform calculations and menu operations quickly for the intended small-scale student dataset.

### NFR6 - Scalability
The modular structure should allow additional features such as persistent storage, database integration, GUI, and academic analytics to be added in future versions.