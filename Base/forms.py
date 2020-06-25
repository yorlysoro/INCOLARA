from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Cuenta, Sectores
class FormularioLogin(AuthenticationForm):
	def __init__(self, *args, **kwargs):
	    super(FormularioLogin, self).__init__(*args,**kwargs)
	    self.fields['username'].widget.attrs['class'] = 'form-control'
	    self.fields['username'].widget.attrs['placeholder'] = 'Coloque su Usuario...'
	    self.fields['password'].widget.attrs['class'] = 'form-control'
	    self.fields['password'].widget.attrs['placeholder'] = 'Coloque su contraseña...'

class FormularioCuenta(forms.ModelForm):

	class Meta:
		model = Cuenta
		fields = ('usuario', 'domicilio', 'rif', 'movil', 'local', 'correo', 'pagina', 'sector')
		labels = {
			'sector' : 'Sector',
		}
		wigets = {
			'sector' : forms.Select(
				attrs = {
					'class' : 'standardSelect',
					'data-placeholder' : 'Seleccion su Sector'
				}
			)
		}
class FormularioSectores(forms.ModelForm):

	class Meta:
		model = Sectores
		fields = ('sector', 'nombre', 'nombre_completo')