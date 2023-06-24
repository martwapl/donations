from django.shortcuts import render
from django.views import View

# Create your views here.
class LandingPage(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

class Register(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

class AddDonation(View):
    template_name = "form.html"

    def get(self, request):
        return render(request, self.template_name)
