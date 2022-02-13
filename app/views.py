from django.shortcuts import render
from app.models import Contact, Portfolio, Project
from django.core.mail import send_mail
from django.contrib.auth.models import User

def home(request):
  project_img = Portfolio.objects.all()
  project = Project.objects.all()

  print(project_img)

  data = {
    'project_img':project_img,
    'project':project
  }

  return render(request,'index.html', data)

def contact(request):
  if request.method=='POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    contact = Contact(name=name, email=email, phone=phone, message=message)
    contact.save()
    users = User.objects.get()
    admin_email = users.email
    messages = (f'you have new message {message}')
    send_mail(f'form {email}', messages, 'Hi Rahul', [admin_email], fail_silently=False)

  return render(request,'index.html')