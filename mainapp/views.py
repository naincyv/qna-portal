from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, SignUpForm


def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'main/post_question.html', {'form': form})


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answers.all()
    form = AnswerForm()
    return render(request, 'main/question_detail.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def post_answer(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
    return redirect('question_detail', id=id)

@login_required
def like_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question_detail', id=answer.question.id)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    # Optional: Only allow the author to delete
    if request.user == question.user:
        question.delete()
    return redirect('home')