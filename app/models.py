from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    portfolio_image = models.ImageField(upload_to='portfolio/')
    about_image = models.ImageField(upload_to='portfolio/')

class Project(models.Model):
    project_thumbnail = models.ImageField(upload_to='project/')
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    project_url = models.URLField(max_length=200)