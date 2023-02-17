import django.views.generic.edit
from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy

app_name = 'sitejail'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='main-page/Login.html'), name='login'),
    path('change_password/', auth_view.PasswordChangeView.as_view()),
    path('gigi/', django.views.generic.edit.CreateView.as_view(form_class=UserCreationForm, template_name='main-page/Login.html', success_url=reverse_lazy("sitejail:login"))),
]