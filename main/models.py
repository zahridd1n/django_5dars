from django.db import models

class Header(models.Model):
    logo_name = models.CharField(max_length=15)
    title = models.CharField(max_length=40)
    sub_title = models.CharField(max_length=50)


class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    web_site = models.URLField()
    img = models.ImageField(upload_to='about-me/')


class Education(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    major = models.CharField(max_length=50)
    university = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    detail = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.SmallIntegerField()


class Experience(models.Model):
    stat = models.IntegerField()
    end = models.IntegerField(null=True,default='Present')
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    detail = models.TextField()

class Profiles(models.Model):
    icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=20)
    url = models.URLField()


class Portfolio(models.Model):
    img = models.ImageField(upload_to='portfolio/')
    name = models.CharField(max_length=50)
    url = models.URLField()

class Client(models.Model):
    img = models.ImageField(upload_to='client/')
    url = models.URLField()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()




