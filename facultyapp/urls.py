from django.urls import path, include
from . import views
app_name = 'facultyapp'
urlpatterns = [
    path('FacultyHomePage/', views.FacultyHomePage, name="FacultyHomePage"),
    path('add_course/', views.add_course, name="add_course"),
    path('view_student_list/', views.view_student_list, name="view_student_list"),
    path('post_marks/', views.post_marks, name="post_marks"),
    path('marks_success/', views.marks_success, name="marks_success"),
]