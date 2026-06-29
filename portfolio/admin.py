from django.contrib import admin
from .models import (
    Skill, Project, ProjectScreenshot, Experience,
    Education, Certification, Achievement, ContactMessage
)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'display_order')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('proficiency', 'display_order')

class ProjectScreenshotInline(admin.TabularInline):
    model = ProjectScreenshot
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'is_featured', 'display_order')
    list_filter = ('is_featured',)
    search_fields = ('title', 'tech_stack', 'description')
    list_editable = ('is_featured', 'display_order')
    inlines = [ProjectScreenshotInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration', 'display_order')
    search_fields = ('role', 'company', 'description')
    list_editable = ('display_order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'branch', 'institution', 'duration', 'display_order')
    search_fields = ('degree', 'institution')
    list_editable = ('display_order',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date', 'display_order')
    search_fields = ('title', 'issuing_organization')
    list_editable = ('display_order',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'ranking_details', 'display_order')
    search_fields = ('title', 'description')
    list_editable = ('display_order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
