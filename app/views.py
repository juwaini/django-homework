from .models import Employee, Company


def get_name_and_company():
    employees = Employee.objects.all()

    for employee in employees:
        print("Name: %s, Company: %s" % (employee.name, employee.company.name))


def get_employee_name_older_than_50():
    employees = Employee.objects.filter(age__gt=50)

    for employee in employees:
        print('Name: %s' % employee.name)


