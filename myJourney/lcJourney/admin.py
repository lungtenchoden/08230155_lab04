from django.contrib import admin
from .models import LearningTopic, Milestone, AboutMe

# Register your models here.

# Inline milestones inside each LearningTopic for convenience
class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1  # allows adding new milestones directly in LearningTopic admin


@admin.register(LearningTopic)
class LearningTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'date_completed')
    search_fields = ('title',)
    inlines = [MilestoneInline]


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'achieved_on')
    list_filter = ('topic', 'achieved_on')
    search_fields = ('title', 'description')


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'bio')
