from django.contrib import auth
from django.shortcuts import render, redirect


def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')
from django.contrib.auth.models import User
from facultyapp.models import Marks
from adminapp.models import StudentList

def view_marks(request):
    user=request.user
    try:
        student_user = User.objects.get(username=user.username)
        student = StudentList.objects.get(Register_Number=student_user)
        marks = Marks.objecct.filter(student=student)
        return render(request, 'studentapp/view_marks,html')
    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request, 'studentapp/no_studentlist.html', {'error':'No studentrecord found for this user.'
                                                                  })
def logoutpagelogic(request):
    auth.logout(request)  # Logs out the user
    return redirect('projecthomepage')  # Redirect to the homepage or desired URL

