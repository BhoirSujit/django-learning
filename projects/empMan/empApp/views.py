from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeeData(req) :
    employees = Employee.objects.all()
    empdict = {"employees" : employees}
    return render(req, 'Employee.html', empdict) 
