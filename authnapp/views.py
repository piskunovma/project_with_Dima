from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.conf import settings

from authnapp.forms import ServiceUserLoginForm, ServiceUserRegisterForm, ServiceUserEditForm


def login(request):
    title = "вход"

    login_form = ServiceUserLoginForm(data=request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))

def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = ServiceUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))

    register_form = ServiceUserRegisterForm()
    content = {"title": title, "register_form": register_form}
    return render(request, "authnapp/register.html", content)


def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = ServiceUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
            
    edit_form = ServiceUserEditForm(instance=request.user)
    content = {"title": title, "edit_form": edit_form, "media_url": settings.MEDIA_URL}
    return render(request, "authnapp/edit.html", content)


    # Вопросы:
    # instance
    # request.POST
