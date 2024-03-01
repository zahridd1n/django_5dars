from django.shortcuts import render
from . import  models
def index(request):
    header = models.Header.objects.last()
    about_me = models.AboutMe.objects.last()
    education = models.Education.objects.all()
    skills = models.Skill.objects.all()
    experiences = models.Experience.objects.all()
    profiles = models.Profiles.objects.all()
    portfolio = models.Portfolio.objects.all()
    clients = models.Client.objects.all()

    context = {
        'header': header,
        'about_me': about_me,
        'educations':education,
        'skills':skills,
        'experiences':experiences,
        'profiles':profiles,
        'portfolio':portfolio,
        'clients':clients,

    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        models.Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
    return render(request, 'index.html', context)
