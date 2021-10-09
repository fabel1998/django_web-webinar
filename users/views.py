from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, CommentAdd
from django.contrib import auth
from .models import Comment, User


# Create your views here.
# контроллеры = views = функции

def index(request):
    if 'btn_nm' in request.POST:
        return HttpResponseRedirect(reverse('users:register'))
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:platform'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:index'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def platform(request):
    comments = User.objects.order_by('id')
    comment_form = CommentAdd()
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        comment_form = CommentAdd(data=request.POST or None)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse('users:platform'))
    context = {
        'comments': comments,
        'comment_form': comment_form,

    }
    return render(request, 'users/platform.html', context)
