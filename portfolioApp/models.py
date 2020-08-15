from django.db import models

import os
def get_upload_path(instance, filename):
    return os.path.join("%s" % instance.vocab.name, filename)

# Create your models here.
class Navbar(models.Model):
    n_name = models.CharField(max_length=30)
    n_link = models.TextField(blank=True, null=True)


class Client_Name(models.Model):
    client_name = models.CharField(max_length=50)
    brand_logo = models.ImageField()

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    message = models.TextField()

class Number_Area(models.Model):
    area_icon = models.CharField(max_length=50)
    area_value = models.IntegerField()
    area_type_description = models.CharField(max_length=100)

class Personal_Information(models.Model):
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    facebook = models.TextField()
    linkedin = models.TextField()
    github = models.TextField()
    twitter = models.TextField()

class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resume = models.FileField(upload_to='resume/')
    image = models.ImageField()

class Project(models.Model):
    p_name = models.CharField(max_length=50)
    p_description = models.CharField(max_length=120)
    p_image = models.ImageField()
    client = models.CharField(max_length=50)
    completed = models.DateField()
    p_type = models.CharField(max_length=50)
    link = models.TextField()

class Services(models.Model):
    s_title = models.CharField(max_length=50)
    s_description = models.CharField(max_length=500)
    s_logo = models.CharField(max_length=50)

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    percentage = models.IntegerField()

class Testimonial(models.Model):
    t_image = models.ImageField()
    t_name = models.CharField(max_length=50)
    t_role = models.CharField(max_length=50)
    t_description = models.CharField(max_length=200)

