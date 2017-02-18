from .models import Employee, Company


def get_name_and_company():
    employees = Employee.objects.all()

    for employee in employees:
        print("Name: %s, Company: %s" % (employee.name, employee.company.name))
        