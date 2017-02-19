from .serializers import CompanySerializer, EmployeeSerializer
from .models import Employee, Company
from rest_framework import viewsets


def get_name_and_company():
    employees = Employee.objects.all()

    for employee in employees:
        print("Name: %s, Company: %s" % (employee.name, employee.company.name))


def get_employee_name_older_than_50():
    employees = Employee.objects.filter(age__gt=50)

    for employee in employees:
        print('Name: %s' % employee.name)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all company.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
