from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('question/new/', views.post_question, name='post_question'),
    path('question/<int:id>/', views.question_detail, name='question_detail'),
    path('question/<int:id>/answer/', views.post_answer, name='post_answer'),
    path('answer/<int:id>/like/', views.like_answer, name='like_answer'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
]