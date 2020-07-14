from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView, CreateView, DetailView, DeleteView
from .forms import FormularioSectores, FormularioCuenta
from .models import Cuenta, Sectores
# Create your views here.


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
