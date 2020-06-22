from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, UpdateView, ListView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from .forms import FormularioLogin, FormularioCuenta, FormularioSectores
from .models import Cuenta, Sectores
# Create your views here.

class Login(FormView):
	template_name = 'login.html'
	form_class = FormularioLogin
	success_url = reverse_lazy('inicio')

	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self, request, *args, **kwargs):
	    if request.user.is_authenticated:
	        return HttpResponseRedirect(self.get_success_url())
	    else:
	        return super(Login, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
	    login(self.request, form.get_user())
	    return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('login')

class Inicio(TemplateView):
	template_name = 'index.html'


class MiCuenta(UpdateView):
	model = Cuenta
	form_class = FormularioCuenta
	template_name = 'Base/mi_cuenta.html'
	success_url = reverse_lazy('inicio')

class SectoresListar(ListView):
	model = Sectores
	template_name = 'Base/sectores_list.html'