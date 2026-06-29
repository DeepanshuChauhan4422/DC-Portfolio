from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('ai_development', 'AI Development'),
        ('devops', 'DevOps'),
        ('computer_science', 'Computer Science'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(help_text="Proficiency percentage (e.g. 90)")
    icon_class = models.CharField(max_length=100, blank=True, help_text="Devicon/FontAwesome class (e.g., 'devicon-python-plain colored')")
    icon_svg = models.TextField(blank=True, help_text="Raw SVG XML code for custom icons")
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(help_text="Short description for the project grid card")
    detailed_description = models.TextField(help_text="Comprehensive details for the project modal")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated values (e.g., 'Django, Python, PostgreSQL, Docker')")
    key_features = models.TextField(help_text="Newline-separated list of key features")
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    architecture_diagram = models.ImageField(upload_to='architecture/', blank=True, null=True)
    challenges_faced = models.TextField(blank=True)
    future_improvements = models.TextField(blank=True)
    is_featured = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order', '-id']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]

    def get_features_list(self):
        return [feature.strip() for feature in self.key_features.split('\n') if feature.strip()]


class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='project_screenshots/')
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Screenshot for {self.project.title}"


class Experience(models.Model):
    company = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    duration = models.CharField(max_length=100, help_text="e.g., 'July 2024 - Present' or 'Jan 2024 - Jun 2024'")
    description = models.TextField(help_text="Newline-separated list of responsibilities/achievements")
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order', '-id']

    def __str__(self):
        return f"{self.role} at {self.company}"

    def get_description_list(self):
        return [item.strip() for item in self.description.split('\n') if item.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    academic_journey = models.TextField(help_text="Description of your academic accomplishments")
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.degree} ({self.branch}) - {self.institution}"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=100)
    credential_link = models.URLField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order', '-id']

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ranking_details = models.CharField(max_length=150, blank=True, help_text="e.g., '4th Rank out of 500 participants'")
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
