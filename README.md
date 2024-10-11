  The code consists of three Python files: `employee.py`, `main.py`, and `staff.py`, which together implement a simple employee management system. 
The company consisted of three types of employees: Salaried, freelancer and stundents. Each type have different configuration.
Salaried employee: Standar salary plus level position: Director +500, Leader +350, Senior +200, Mid +100, Junior +0.
Freelancer: Standar salaryadds plus overtime: overtime rate * overtime.
Stundents: For ages twenty-five and older give salaries different as younger.

### 1. `employee.py`:
This file defines the base structure of employees and how their salaries and roles are managed.

- **Employees class**: 
   - Manages a list of objects.
   - Methods:
     - `total_expenses()`: Calculates the total salary expenses.
     - `average_expenses()`: Calculates the average salary across all employees.
  
- **Employee (abstract base class)**: 
   - Basic structure for any employee with attributes such as first name, last name, position, and salary.
   - `give_raise()`: Increases the salary of an employee by a given amount.
  
- **SalariedWorker (inherits from Employee)**: 
   - Represents a salaried worker with additional attributes like level (Junior, Mid, Senior, etc.).
   - `total_salary()`: Calculates the worker's salary with level-based increments.
   - `display_info()`: Displays worker details that formatted for the "pretty table", including salary and position.

- **FreelancerEmployee (inherits from Employee)**: 
   - Represents a freelancer with different salary structure (includes hourly wages).
   - `overtime_increment()`: Calculate overtime salary depend on overtime and overtime price.
   - `total_salary()`: Calculates the freelancer's total salary with overtime.
   - `display_info()`:Displays freelancer details that formatted for the "pretty table", including overtime and overtime price.

- **Stundents**:
   - Represents a student .
   - `total_salary()`: Calculates the worker's salary depend on age.
   - `display_info()`: Displays student details that formatted for the "pretty table".

### 2. `main.py`:
This file contains logic to create employee objects and interact with the system.

- It seems to generate data, possibly to populate the employee system for testing or demonstration purposes. Data includes salaried workers, freelancers and students, with attributes such as name, salary, position, overtime, age and experience level.

### 3. `staff.py`:
Defines specific instances of employees, including:

- **Salaried**: A list of employees is created with attributes such as name, position, salary, and experience level.
- **Freelancer**: A list of employees is created with attributes such as name, position, salary, overtime rate and overtime.
- **Students**: Likely for an internship or training scenario, with attributes including age but no salary.

Together, the system calculates the total and average expenses for employees, manages salaries, and supports operations for both full-time salaried workers and freelancers.
