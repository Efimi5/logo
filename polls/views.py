from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.


# class RegisterFormView(FormView):
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/login/"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "register.html"

#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()

#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)

def register(request):
    if request.method == 'GET':
        user_form = UserRegistrationForm(request.GET)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'polls/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'user_form': user_form})