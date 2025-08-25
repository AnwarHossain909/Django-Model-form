from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'student_list.html', {'form': form, 'students': students})


def student_update(request, pk):   # <-- নতুন function
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


def student_delete(request, pk):   # <-- optional delete
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('/')
