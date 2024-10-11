from employee import SalariedWorker, FreelancerEmployee, StudentEmployee, Employees
from prettytable import PrettyTable
from staff import salaried, freelancers, students


def make_objects(type_list_employee):
    objects_list = []
    if type_list_employee == salaried:
        for sal in salaried:
           temp = SalariedWorker(sal['first_name'], sal['last_name'], sal['position'], sal['salary'], sal['level'])
           objects_list.append(temp)
    elif type_list_employee == freelancers:
        for fre in freelancers:
            temp = FreelancerEmployee(fre['first_name'], fre['last_name'], fre['position'], fre['salary'],
                                      fre['salary_per_overtime'], fre['overtime'])
            objects_list.append(temp)
    elif type_list_employee == students:
        for stu in students:
            temp = StudentEmployee(stu['first_name'], stu['last_name'], stu['position'], stu['salary'], stu['age'])
            objects_list.append(temp)
    return objects_list

obj_list_salaried = make_objects(salaried)
obj_list_freelancers = make_objects(freelancers)
obj_list_students = make_objects(students)
employee_list = obj_list_salaried + obj_list_freelancers + obj_list_students
employees = Employees(employee_list)

table = PrettyTable()
table.title = 'list of staff'.upper()
table.field_names = ["First name", "Last name", "Position", "Type of employee", "Salary", "Level increment",
                     "Overt. incr. (value * hours)","Total salary"]

for temp in employee_list[0:-1]:
    table.add_row(temp.display_info())
table.add_row(employee_list[-1].display_info(), divider=True)

table.add_row(["","","","","","", "Total Expenses", round(employees.total_expenses(),2)],divider=True)
table.add_row(["","","","","","", "Salaried average expenses", round((Employees(obj_list_salaried)).average_expenses(),2)],divider=True)
table.add_row(["","","","","","", "Freelancers average expenses", round((Employees(obj_list_freelancers)).average_expenses(),2)],divider=True)
table.add_row(["","","","","","", "Students average expenses", round((Employees(obj_list_students)).average_expenses(),2)])
print(table)
