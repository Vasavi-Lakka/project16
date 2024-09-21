from django.db import models # type: ignore

# Create your models here.
class Dept(models.Model):
    deptNo=models.IntegerField(primary_key=True)
    dName=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
class Emp(models.Model):
    empNo=models.PositiveIntegerField()
    eName=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    MGR=models.IntegerField(null=True)
    hireDate=models.DateField()
    salary=models.DecimalField(max_digits=100,decimal_places=5)
    comm=models.DecimalField(max_digits=100,decimal_places=5,null=True)
    deptNo=models.ForeignKey(Dept, on_delete=models.CASCADE)