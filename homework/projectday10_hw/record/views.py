from .models import Student
# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentForm  

def student_list(request):
    query=request.GET.get('q','')
    students=Student.objects.filter(name__icontains=query)
    return render(request, 'student_list.html', {'students': students, 'query': query})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list') 
    else:
        form = StudentForm()
    
    return render(request, 'student_form.html', {'form': form})

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  
    return render(request, 'student_delete.html', {'student': student})
