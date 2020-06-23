from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DetailView, DeleteView
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
	context_object_name = 'Sectores_List'
	template_name = 'Base/sector_list.html'

class SectoresCrear(CreateView):
	model = Sectores
	form_class = FormularioSectores
	context_object_name = 'Sector'
	template_name = 'Base/sector_crear.html'
	success_url = reverse_lazy('Base:lista_sectores')

class SectoresEditar(UpdateView):
	model = Sectores
	form_class = FormularioSectores
	template_name = 'Base/sector_editar.html'
	
	def get_success_url(self):
		return reverse_lazy('Base:sector_detalle', kwargs={ 'pk' : self.object.id })


class SectoresDetalle(DetailView):
	model = Sectores
	form_class = FormularioSectores
	context_object_name = 'sector'
	template_name = 'Base/sector_detalle.html'


class SectoresBorrar(DeleteView):
	model = Sectores
	template_name = 'Base/sector_borrar.html'
	success_url = reverse_lazy('Base:lista_sectores')
