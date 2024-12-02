from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('creator', 'Survey Creator'),
        ('taker', 'Survey Taker'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        related_name='survey_app_user_groups',  # Add related_name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='survey_app_user_permissions',  # Add related_name to avoid conflict
        blank=True,
    )

# Survey model
class Survey(models.Model):
    STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('closed', 'Closed'),
    ('republished', 'Republished'),
]
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="surveys")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Question model
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    is_multiple_choice = models.BooleanField(default=False)

# Option model
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)

# Response model
class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="responses")
    taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
