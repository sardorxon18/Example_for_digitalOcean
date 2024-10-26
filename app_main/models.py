from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
# class comment\

class Education(models.Model):
    education=models.CharField(max_length=50)
    specialist=models.CharField(max_length=200)
    discription=models.TextField()
    time=models.CharField(max_length=  11)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.education
    
class Expericence(models.Model):
    c_name=models.CharField(max_length=100)
    position=models.CharField(max_length=200)
    time=models.CharField(max_length=  11)
    discription=models.TextField()
    salary=models.IntegerField(blank=True,null=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateField(auto_now=True)

    def __str__(self):
        return self.c_name
    

class Skills(models.Model):
    name=models.CharField(max_length=100)
    degre= models.IntegerField(max_length=100)

    def __str__(self):
        return self.c_name


class Testimonial(models.Model):
    name=User.first_name
    position=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)
    client_say = models.TextField()
    image=models.ImageField(upload_to='clients/',default='media/account.png',blank=True,null=True)
    confirm=models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.name} \t {self.client_say[10]}"
    
class Blogs(models.Model):
    thema = models.CharField(max_length=100)
    image=models.ImageField(upload_to='blogs/',blank=True,null= True)
    body= models.TextField()
    