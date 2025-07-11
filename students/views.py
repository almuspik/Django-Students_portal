from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student

def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)  
    if form.is_valid():
        form.save()
        return render(request, 'add_student.html', {'form': StudentForm(), 'success': True})
    return render(request, 'add_student.html', {'form': form})



def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('view_all_students')

def search_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        reg_no = request.POST.get('reg_no')
        student = Student.objects.filter(name=name, reg_no=reg_no).first()
        if student:
            return render(request, 'student_detail.html', {'student': student})
        else:
            return render(request, 'search_student.html', {'error': 'Student not found'})
    return render(request, 'search_student.html')


def home(request):
    return render(request, 'home.html')
    from .models import Student

def view_all_students(request):
    students = Student.objects.all().order_by('name')  
    return render(request, 'view_all.html', {'students': students})
