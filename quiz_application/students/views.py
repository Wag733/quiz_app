from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from students.models import Student, QuizResult
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from admins.models import Quiz
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from admins.models import Quiz, Question, Choice
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def available_quizzes(request):
    student = request.user.student
    quizzes = student.quizzes.filter(due_date__gt=timezone.now())
    return render(request, 'students/available_quizzes.html', {'quizzes': quizzes})

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        total_questions = questions.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = get_object_or_404(Choice, id=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1

        score_percentage = (score / total_questions) * 100
        QuizResult.objects.create(student=request.user.student, quiz=quiz, score=score_percentage)
        messages.success(request, f'Quiz submitted successfully. Your score: {score_percentage}%')
        return redirect('quiz_history')

    return render(request, 'students/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_history(request):
    student = request.user.student
    quiz_results = QuizResult.objects.filter(student=student)
    return render(request, 'students/quiz_history.html', {'quiz_results': quiz_results})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user)  # Create a student profile
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')






@login_required
def student_profile(request):
    student = request.user.student
    if request.method == 'POST':
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=student)
        password_form = PasswordChangeForm(request.user, request.POST)
        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            return redirect('student_profile')
    else:
        profile_form = StudentProfileForm(instance=student)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'students/student_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
        'username': request.user.username
    })

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')
