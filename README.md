# Testing_projects
## The program solves this task in four diferent ways:
- BestUni University consists of two faculties: Engineering and Art and Science. 
- The campus has four buildings labeled A, B, C, and D. The software specifications for course building allocation are as follows:
    - If the number of registered students is less than 10 in the Engineering Faculty, the course will be held in building A.
    - If the number of registered students is between 10 and 50 in the Engineering Faculty, the course will be held in building B.
    - For the Art and Science Faculty, if the number of registered students is less than 10, the course will be held in building B.
    - If the number of registered students is between 10 and 50, the course will be held in building C.
    -   If the number of registered students is greater than 50 for both faculties, the course will be held in building D.
### The same in a table
| enginner_students | art_science_students | Building result |
|-------------------|----------------------|-----------------|
| <10               |                      | A               |
| between 10-50     |                      | B               |
|                   | <10                  | B               |
|                   | between 10-50        | C               |
| >50               | >50                  | D               |

## The goal is
- Tested this program
- Created bugs for this implementations that are difficult to see
    - *bad functions
- Minimize tests which can detect these bugs