import base64
import string
from io import BytesIO

import pandas as pd
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from matplotlib import pyplot as plt


def ProjectHomePage(request):
    return render(request, 'adminapp/ProjectHomePage.html')
def printpagecall(request):
    return render(request, 'adminapp/printer.html')
def printpagelogic(request):
    if request.method == "POST":
        User_input = request.POST['User_input']
        print(f'User input: {User_input}')
    a1 = {'User_input': User_input}
    return render(request, 'adminapp/printer.html', a1)

def exceptionpagelogic(request):
    if request.method == "POST":
        User_input = request.POST['User_input']
        result = None
        error_message = None
        try:
            num = int(User_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')



from .forms import *
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')
def UserRegisterPageCall(request):
    return render(request, 'adminapp/Register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
        email = request.POST['Email_ID']
        pass1 = request.POST['Password']
        pass2 = request.POST['Confirm_Password']
        print(username)
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')
from django.contrib import messages
from django.contrib.auth import authenticate,login

def UserLoginPageCall(request):
    return render(request,'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/Login.html')
    else:
        return render(request, 'adminapp/Login.html')
def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')

#def add_student(request):
 #   if request.method == 'POST':
  #      form = StudentForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('student_list')
    #else:
     #   form = StudentForm()
    #return render(request, 'adminapp/add_student.html', {'form':form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html',{'students': students})

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')
import datetime
import calendar
from datetime import timedelta

from datetime import datetime, timedelta
import calendar
from django.shortcuts import render


def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not a Leap Year"
        else:
            ran3 = "Leap Year"
        a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    else:
        a1 = {'ran': None, 'ran3': None, 'ran1': None, 'number1': None}
    return render(request, 'adminapp/datetimepage.html', a1)

import random
import string
def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/randomexample.html', a1)

import random
import string
def randomlogic(request):

    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/randomexample.html', a1)

def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')
def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm

# View to list contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'adminapp/add_contact.html', {'contacts': contacts})

# View to add a contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send contact info to a specified email if requested
            if 'send_email' in request.POST:
                recipient_email = request.POST.get('recipient_email')
                send_mail(
                    subject='New Contact Created',
                    message=f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone_number}\nAddress: {contact.address}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient_email],
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

# View to delete a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('ProjectHomePage')  # Redirect to the same page after submission
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/feedback_form.html', {'form': form})


class UploadFileForm:
    pass


def upload_file(request):
    if request .method=='POST' and request.FILES['sales_data.csv3']:
        file=request.FILES['sales_data.csv']
        df=pd.read_csv(file,parse_dates=['Date'],dayfirst=True)
        total_sales=df['Sales'].sum()
        average_sales=df['Sales'].mean()
        df['Month']=df['Date'].dt.month
        monthly_sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
        plt.pie(monthly_sales,labels=monthly_sales.index,autopct='%1.1f%%')
        plt.title('Sales distribution per month ')
        from io import BytesIO
        buffer=BytesIO()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_data=base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request,'adminapp/chart.html',{
            'total_sales':total_sales,
            'average_sales':average_sales,
            'chart':image_data
        })
    return render(request,'adminapp/chart.html',{'form':UploadFileForm})

def add_student_page_call(request):
    return render(request, 'adminapp/AddStudent.html')