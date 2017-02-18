# django-homework
Assignment on Django

Given the following models

class Company(models.Model):
     name = models.CharFied(max_length=100)

class Employee(models.Model):
     name = models.CharFied(max_length=100)
     age = models.IntegerField()
     company = models.ForeginKey(Company)


write code that would print name of each employee in the system as well as their company name.

print employee names who are older than 50 years old

create the function Company.objects.big_companies() that return  list of companies that has at least 20

make changes to the big_companies function above so that code like this can work Company.objects.big_companies().filter(name__startswith="A")

Create a model serializer class and viewset for Company model

Create a model serializer class and viewset for Employee model that accept company id as GET argument and return employees for this company only
