from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignUpForm

# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("home")
