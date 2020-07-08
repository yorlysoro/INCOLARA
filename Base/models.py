from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from INCOLARA.settings import MEDIA_URL, STATIC_URL
# Create your models here.
SECTORES_CHOICE = [
	('S1','Sector Primario'),
	('S2','Sector Secundario'),
	('S3','Sector Terciario'),
	('S4','Sector Cuaternario'),
]
class Sectores(models.Model):
	sector = models.CharField('Sector', max_length=255, choices=SECTORES_CHOICE)
	nombre = models.CharField('Nombre', max_length=255)
	nombre_completo = models.CharField('Nombre Completo', max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Sector"
		verbose_name_plural = "Sectores"
	def __str__(self):
		return self.sector + "--" + self.nombre + "--" + self.nombre_completo

class Cuenta(AbstractUser):
	domicilio = models.CharField('Domicilio de la Compania', max_length=255, null=True, blank=True)
	rif = models.CharField('Registro de Informacion Fiscal', max_length=255, null=True, blank=True)
	movil = models.CharField('Telefono Movil', max_length=12, null=True, blank=True)
	local = models.CharField('Telefono Fijo', max_length=12, null=True, blank=True)
	pagina = models.URLField('Pagina Web', null=True, blank=True)
	sector = models.ForeignKey(Sectores, null=True, blank=True, on_delete=models.SET_NULL)
	logo = models.ImageField(upload_to='media/cuentas', null=True, blank=True)

	def get_logo(self):
		if self.logo:
			return '{}{}'.format(MEDIA_URL, self.logo)
		return '{}{}'.format(STATIC_URL, 'images/empty.png')


	class Meta:
		verbose_name = "Cuenta"
		verbose_name_plural = "Cuentas"

	def __str__(self):
		return str(str(self.rif) + "--" + str(self.first_name))

