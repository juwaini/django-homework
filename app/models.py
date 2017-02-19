from django.db import models
from django.db.models import Count


class CompanyManager(models.Manager):
    def big_companies(self):
        def get_queryset(self):
            return super(CompanyManager, self).get_queryset()
        return Company.objects.annotate(ep=Count('employee')).filter(ep__gt=20)


class Company(models.Model):
    name = models.CharField(max_length=100)
    objects = CompanyManager()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    company = models.ForeignKey(Company)
