# Testing_projects
## The program solves this task in four different ways:
- BestUni University consists of two faculties: Engineering and Art and Science. 
- The campus has four buildings labeled A, B, C, and D. The software specifications for course building allocation are as follows:
    - If the number of registered students is less than 10 in the Engineering Faculty, the course will be held in building A.
    - If the number of registered students is between 10 and 50 in the Engineering Faculty, the course will be held in building B.
    - For the Art and Science Faculty, if the number of registered students is less than 10, the course will be held in building B.
    - If the number of registered students is between 10 and 50, the course will be held in building C.
    - If the number of registered students is greater than 50 for both faculties, the course will be held in building D.
    - If the sum of the students are over 50 then the bigger group has to move to building D.
### The same in a table
| engineer_students | art_science_students | Building result               |
|-------------------|----------------------|-------------------------------|
| <10               |                      | engineer: A                   |
| between 10-50     |                      | engineer: B                   |
|                   | <10                  | art_science: B                |
|                   | between 10-50        | art_science: C                |
| >50               | >50                  | both: D                       |
| x                 | y                    | x+y>50 -> bigger group: D |

## The goal is
- Test this program
- Create bugs for this implementations that are difficult to see
    - Implemented these in *bad functions
- Minimize tests which can detect these bugs