from django.shortcuts import render
from django.core.paginator import Paginator
from random import choice

tags = ['Android_Studio', 'Activity', 'Kotlin', 'JDK', 'Python', 'scrcpy']

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Text {i}',
        'rating': 0,
        'tags': sorted([choice(tags) for each in range(2)])
    } for i in range(100)
]


def paginate(objects, page, per_page=10):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)


def index(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, per_page=10)
    try:
        if int(page) > paginator.num_pages:
            page = 1
    except ValueError:
        page = 1
    questions = paginator.page(page)
    return render(request, "index.html",
                  {'questions': questions, 'paginator': paginator, 'page': int(page)})


def question(request, question_id):
    this_question = QUESTIONS[question_id]
    return render(request, 'oneQuestionAndAnswers.html', {'questions': this_question})


def new_question(request):
    return render(request, 'newQuestion.html')


def sign_up(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def settings(request):
    return render(request, 'settings.html')


def tag_view(request, tag):
    tags_view = [tag_question for tag_question in QUESTIONS if tag in tag_question['tags']]
    page = request.GET.get('page', 1)
    paginator = Paginator(tags_view, per_page=10)
    try:
        if int(page) > paginator.num_pages:
            page = 1
    except ValueError:
        page = 1
    questions = paginator.page(page)
    return render(request, 'tagQuestions.html',
                  {'questions': questions, 'tag': tag, 'paginator': paginator, 'page': int(page)})


def hot_questions(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(QUESTIONS, per_page=10)
    try:
        if int(page) > paginator.num_pages:
            page = 1
    except ValueError:
        page = 1
    questions = paginator.page(page)
    return render(request, 'hotQuestions.html',
                  {'questions': questions, 'paginator': paginator, 'page': int(page)})


def error_not_found(request):
    return render(request, '404page.html')
