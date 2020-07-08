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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'
		self.fields['first_name'].widget.attrs['autofocus'] = True
		self.fields['sector'].widget.attrs['class'] = 'standardSelect'


	class Meta:
		model = Cuenta
		fields = ('first_name', 'domicilio', 'rif', 'movil', 'local', 'email', 'pagina', 'sector', 'logo')
		
class FormularioSectores(forms.ModelForm):

	class Meta:
		model = Sectores
		fields = ('sector', 'nombre', 'nombre_completo')