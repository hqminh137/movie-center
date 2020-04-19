from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView
from .forms import (
    LoginForm,
    RegisterForm
)


class SiteLoginView(LoginView):
    template_name = "account/login.html"


class SiteSignupView(FormView):
    template_name = 'account/signup.html'
    form_class = RegisterForm


# class EditProfileView():
#     pass
#

# def signup(request):
#     form = UserSignUpForm()
#     if request.method == "POST":
#         form = UserSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#     return render(request, "account/signup.html", {"form": form})
#
#
# def change_password(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, ("mat khau da duoc cap nhat!"))
#             return HttpResponseRedirect("/account/password_change_done")
#         else:
#             messages.error(request, ("Please correct the error below."))
#             return HttpResponseRedirect("/account/password_change_fail")
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, "account/change_password.html", {"form": form})
#
#
# def password_change_done(request):
#     return render(request, "account/password_change_done.html")
#
#
# def password_change_fail(request):
#     return render(request, "account/password_change_fail.html")
