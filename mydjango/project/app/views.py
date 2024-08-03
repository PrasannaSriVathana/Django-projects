from django.shortcuts import render
from app.models import Student
from .forms import StudentForm

# Create your views here.
def st(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        people = Student.objects.all()
        if form.is_valid():
            form.save()
            return render(req,'success.html',{'form':form,'people':people})
    else:
        form=StudentForm()
        return render(req,'student.html',{'form':form})