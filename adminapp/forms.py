from django import forms
from django import forms
from .models import Task, Feedback


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

from.models import StudentList
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']

        # Optional: Add widgets to style the form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']

# forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
