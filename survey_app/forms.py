from django import forms
from .models import Survey, Question, Option, User

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'is_multiple_choice']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
