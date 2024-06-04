from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from sales.models import Client, History
from users.forms import LoginUserForm, ProfileUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}

    def get_success_url(self):
        return reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class Orders(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'users/orders.html'
    context_object_name = 'orders'

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        a = History.objects.all().filter(client_id=self.request.user.id - 1).select_related('client')
        return a

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Покупки'})
        return context


class Home(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'users/index.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(email=self.request.user.email)
        title = "Профиль " + self.request.user.first_name
        context.update({'title': title, 'client': client})
        return context
