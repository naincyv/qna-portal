from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
            'description': forms.Textarea(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
            'email': forms.TextInput(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
            'password1': forms.TextInput(attrs={'class': 'form-control','style': 'font-weight: bold;'}),
            
        }