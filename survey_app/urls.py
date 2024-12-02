from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create_survey/', views.create_or_edit_survey, name='create_survey'),
    path('add_questions_and_options/<int:survey_id>/', views.add_questions_and_options, name='add_questions_and_options'),
    path('edit_survey/<int:survey_id>/', views.create_or_edit_survey, name='edit_survey'),
    path('publish_survey/<int:survey_id>/', views.publish_survey, name='publish_survey'),
    path('close_survey/<int:survey_id>/', views.close_survey, name='close_survey'),
    path('delete_survey/<int:survey_id>/', views.delete_survey, name='delete_survey'),
    path('take_survey/<int:survey_id>/', views.take_survey, name='take_survey'),
    path('view_results/<int:survey_id>/', views.view_results, name='view_results'),
    path('republish_survey/<int:survey_id>/', views.republish_survey, name='republish_survey'),
]
