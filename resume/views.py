from django.shortcuts import render
from .models import Profile, Skill, Experience, Project

def home(request):
    profile = Profile.objects.first()  # Assuming one profile
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    return render(request, 'resume/home.html', {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
    })
