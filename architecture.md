# CampusOS - System Architecture

## 1. System Architecture

                    +------------------+
                    |     main.py      |
                    |   Main Program   |
                    +--------+---------+
                             |
          +------------------+------------------+
          |          |          |        |      |
          v          v          v        v      v
     +---------+ +---------+ +---------+ +---------+
     | Profile | | Subjects| | Attend. | |  Tasks  |
     |  .py    | |  .py    | |  .py    | |   .py   |
     +---------+ +---------+ +---------+ +---------+
          |          |          |        |
          +----------+----------+--------+
                             |
                  +----------+----------+
                  |                     |
                  v                     v
             +---------+          +-------------+
             | Grades  |          |  Dashboard  |
             |  .py    |          |    .py     |
             +---------+          +-------------+
                  |
                  v
             CGPA Calculation

## 2. Program Workflow

                  +---------+
                  |  START  |
                  +----+----+
                       |
                       v
             +-------------------+
             | Enter Student     |
             | Profile Details   |
             +---------+---------+
                       |
                       v
                +-------------+
                |  Main Menu  |
                +------+------+
                       |
       +---------------+---------------+
       |       |       |       |       |
       v       v       v       v       v
   Dashboard Subjects Attend. Tasks  Grades
       |       |       |       |       |
       +-------+-------+-------+-------+
                       |
                       v
                +-------------+
                |   Profile   |
                +------+------+
                       |
                       v
                +-------------+
                |  Main Menu  |
                +------+------+
                       |
                  Exit selected?
                    /       \
                  No         Yes--+
                  |               | 
                  +---> Main      v
                        Menu     END

## 3. Module Responsibilities
main.py - Controls the main program flow and menu.
student_profile.py - Handles student profile information.
subjects.py - Handles subject information.
attendance.py - Calculates and monitors attendance.
tasks.py - Handles academic task management.
grades.py - Handles grade points and CGPA calculation.
dashboard.py - Displays an overview of student information.

## 4. Design Rationale
CampusOS is divided into separate Python modules so that each
module has a specific responsibility. This makes the program 
easier to understand, maintain, test, and extend.

The main program acts as the central controller and calls the required module based on the user's selection.