from django.shortcuts import render
from .models import LearningTopic, Milestone, AboutMe

# Create your views here.


def index(request):
    # Get all learning topics and milestones
    topics = LearningTopic.objects.all().order_by('date_started')
    milestones = Milestone.objects.all().order_by('achieved_on')

    context = {
        'topics': topics,
        'milestones': milestones,
    }
    return render(request, 'index.html', context)


def about_me(request):
    # Get your about-me info (assuming one entry)
    about = AboutMe.objects.first()  # or filter if multiple

    context = {
        'about': about,
    }
    return render(request, 'aboutMe.html', context)

