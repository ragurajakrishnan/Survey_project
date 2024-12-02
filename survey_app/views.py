from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, SurveyForm, QuestionForm, OptionForm
from django.urls import reverse
from .models import Survey, Question, Option, Response, Answer, User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, SurveyForm
from .models import Survey, Question, Option, Response, Answer, User
# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'survey_app/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'survey_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'survey_app/login.html')

# User Logout
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    # Get error message from query parameters, if present
    error = request.GET.get('error', None)

    if request.user.role == 'creator':
        draft_surveys = Survey.objects.filter(creator=request.user, status='draft')
        published_surveys = Survey.objects.filter(creator=request.user, status='published')
        closed_surveys = Survey.objects.filter(creator=request.user, status='closed')
        return render(request, 'survey_app/creator_dashboard.html', {
            'draft_surveys': draft_surveys,
            'published_surveys': published_surveys,
            'closed_surveys': closed_surveys,
            'error': error,  # Pass the error message to the template
        })
    elif request.user.role == 'taker':
        surveys = Survey.objects.filter(status='published')
        return render(request, 'survey_app/taker_dashboard.html', {'surveys': surveys})


@login_required
def publish_survey(request, survey_id):
    # Ensure it's a POST request
    if request.method != 'POST':
        return redirect('dashboard')

    # Fetch the survey object
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user)

    # Validate the current status and question count
    if survey.status != 'draft':
        return redirect(f"{reverse('dashboard')}?error=Only surveys in 'draft' status can be published.")

    if survey.questions.count() < 5:
        return redirect(f"{reverse('dashboard')}?error=Survey must have at least 5 questions to be published.")

    # Update the status
    survey.status = 'published'
    survey.save()

    # Redirect back to the dashboard
    return redirect('dashboard')


@login_required
def close_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user, status='published')
    survey.status = 'closed'
    survey.save()
    return redirect('dashboard')


# Create Survey
@login_required
def create_survey(request):
    if request.user.role != 'creator':
        return redirect('dashboard')
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect('add_questions_and_options', survey_id=survey.id)
    else:
        form = SurveyForm()
    return render(request, 'survey_app/create_survey.html', {'form': form})

# Add Questions and Options
@login_required
def add_questions_and_options(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user)
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('questions-') and key.endswith('-text'):
                question_text = value
                options_key = key.replace('-text', '-options')
                options_text = request.POST.get(options_key, '')
                options = [option.strip() for option in options_text.split(',') if option.strip()]
                if len(options) < 2:
                    return render(request, 'survey_app/add_questions_and_options.html', {
                        'survey': survey,
                        'error': f"Question '{question_text}' must have at least two options."
                    })
                question = Question.objects.create(survey=survey, text=question_text)
                for option_text in options:
                    Option.objects.create(question=question, text=option_text)
        return redirect('dashboard')
    return render(request, 'survey_app/add_questions_and_options.html', {'survey': survey})

# Publish Survey
# @login_required
# def publish_survey(request, survey_id):
#     survey = get_object_or_404(Survey, id=survey_id, creator=request.user, status='draft')
#     if request.method == 'POST':
#         if survey.questions.count() < 5:
#             return render(request, 'survey_app/dashboard.html', {
#                 'error': "Survey must have at least 5 questions to be published."
#             })
#         survey.status = 'published'
#         survey.save()
#         return redirect('dashboard')

@login_required
def create_or_edit_survey(request, survey_id=None):
    survey = None
    if survey_id:
        survey = get_object_or_404(Survey, id=survey_id, creator=request.user)
    
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.status = survey.status or 'draft'  # Default to 'draft' if no status is provided
            survey.save()
            
            # Process questions and options
            question_keys = [key for key in request.POST.keys() if key.startswith('question-') and key.endswith('-text')]
            for question_key in question_keys:
                question_index = question_key.split('-')[1]
                question_text = request.POST.get(question_key)
                question_type = request.POST.get(f'question-{question_index}-type')
                options_text = request.POST.get(f'question-{question_index}-options')

                if question_text and question_type and options_text:
                    question = Question.objects.create(
                        survey=survey,
                        text=question_text,
                        is_multiple_choice=(question_type == 'multiple')
                    )
                    options = [opt.strip() for opt in options_text.split(',') if opt.strip()]
                    for option_text in options:
                        Option.objects.create(question=question, text=option_text)
            return redirect('dashboard')

    return render(request, 'survey_app/create_or_edit_survey.html', {
        'form': SurveyForm(instance=survey),
        'survey': survey,
    })

# Close Survey
@login_required
def close_survey(request, survey_id):
    if request.user.role != 'creator':
        return redirect('dashboard')
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user)
    if survey.status == 'published':
        survey.status = 'closed'
        survey.save()
    return redirect('dashboard')

@login_required
def take_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, status__in=['published', 'republished', 'closed'])
    if survey.status == 'closed':
        return render(request, 'survey_app/survey_closed.html', {'survey': survey})
    
    aggregated_results = None
    if survey.status == 'republished':
        responses = Response.objects.filter(survey=survey)
        total_responses = responses.count()
        aggregated_results = []
        for question in survey.questions.all():
            options_data = []
            for option in question.options.all():
                count = responses.filter(answers__question=question, answers__option=option).count()
                percentage = (count / total_responses * 100) if total_responses > 0 else 0
                options_data.append({'text': option.text, 'count': count, 'percentage': percentage})
            aggregated_results.append({'question': question.text, 'options': options_data})
    
    if request.method == 'POST':
        response = Response.objects.create(survey=survey, taker=request.user)
        for question in survey.questions.all():
            if question.is_multiple_choice:
                selected_option_ids = request.POST.getlist(str(question.id))  # Fetch multiple options
                for option_id in selected_option_ids:
                    Answer.objects.create(response=response, question=question, option_id=option_id)
            else:
                option_id = request.POST.get(str(question.id))  # Fetch single option
                if option_id:
                    Answer.objects.create(response=response, question=question, option_id=option_id)
        return render(request, 'survey_app/survey_completed.html', {'survey': survey})

    return render(request, 'survey_app/take_survey.html', {
        'survey': survey,
        'aggregated_results': aggregated_results,
    })

# View Results
@login_required
def view_results(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user, status__in=['published', 'closed'])
    responses = Response.objects.filter(survey=survey)
    total_responses = responses.count()

    results = []
    for question in survey.questions.all():
        options_data = []
        for option in question.options.all():
            count = responses.filter(answers__question=question, answers__option=option).count()
            percentage = (count / total_responses * 100) if total_responses > 0 else 0
            options_data.append({'text': option.text, 'count': count, 'percentage': percentage})
        results.append({'question': question.text, 'options': options_data})

    return render(request, 'survey_app/results_dashboard.html', {
        'survey': survey,
        'total_responses': total_responses,
        'results': results,
    })

@login_required
def republish_survey(request, survey_id):
    if request.user.role != 'creator':
        return redirect('dashboard')
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user, status='closed')
    survey.status = 'republished'
    survey.save()
    return redirect('dashboard')

# Delete Survey
@login_required
def delete_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, creator=request.user)
    if request.method == 'POST':
        survey.delete()
    return redirect('dashboard')