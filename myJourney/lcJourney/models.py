from django.db import models

# Create your models here.

class LearningTopic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateField()
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    topic = models.ForeignKey(LearningTopic, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=200)
    description = models.TextField()
    achieved_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.topic.title})"



class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='about_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
