from django.db import models

# Create your models here.
from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP','Advanced Object Oriented Programming'),
        ('PFSD','Python Full Stack Development'),

    ]
    SECTION_CHOICES = [
        ('S11','Section1'),
        ('S12', 'Section2'),
        ('S13', 'Section3'),
        ('S14', 'Section4'),
        ('S15', 'Section5'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'
class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]

    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()
    def _str_(self):
        return f"{self.student.name} - {self.course}"