from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext


class CustomLoginRequired(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, gettext('Вы не авторизованы! Пожалуйста, выполните вход.'))
        return redirect(reverse('login'))