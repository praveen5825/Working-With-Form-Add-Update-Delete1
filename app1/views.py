from django.shortcuts import render,redirect
from .models import Employee
from datetime import datetime

# Create your views here.
def show_detail(request):
    Emp=Employee.objects.all()
    context={
        'emp':Emp
    }
    return render(request,'index.html',context)

def Add_new(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        salary=request.POST['salary']
        doj=datetime.now()
        employee=Employee(name=name,age=age,salary=salary,doj=doj,)
        employee.save()
        return redirect("/")
    return render(request,'add_form.html')

def update_form(request, id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        salary=request.POST['salary']
        employee.name=name
        employee.age=age
        employee.salary=salary
        employee.save()
        return redirect("/")
    
    return render(request,'update_form.html',context={'emp':employee,})

def delete_form(request, id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')