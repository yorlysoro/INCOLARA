from allauth.account.forms import LoginForm, SignupForm
from django import forms
from .models import Cuenta, Sectores
class FormularioLogin(LoginForm):
	def __init__(self, *args, **kwargs):
	    super(FormularioLogin, self).__init__(*args,**kwargs)
	    self.fields['login'].widget.attrs['class'] = 'form-control'
	    self.fields['password'].widget.attrs['class'] = 'form-control'


class FormularioRegistro(SignupForm):
	def __init__(self, *args, **kwargs):
		super(FormularioRegistro, self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'

	def save(self, request):
		user = super(FormularioRegistro, self).save(request)
		return user


class FormularioCuenta(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for form in self.visible_fields():
			form.field.widget.attrs['class'] = 'form-control'
			form.field.widget.attrs['autocomplete'] = 'off'
		self.fields['logo'].widget.attrs['class'] = 'input-control'
		self.fields['first_name'].widget.attrs['autofocus'] = True
		self.fields['sector'].widget.attrs['class'] = 'standardSelect'
		#self.fields['sector'].widget.attrs['style'] = 'display: none;'
		self.fields['sector'].widget.attrs['multiple'] = True


	class Meta:
		model = Cuenta
		fields = ('first_name', 'domicilio', 'rif', 'movil', 'local', 'email', 'pagina', 'sector', 'logo')
		
class FormularioSectores(forms.ModelForm):

	class Meta:
		model = Sectores
		fields = ('sector', 'nombre', 'nombre_completo')