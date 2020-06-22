from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
		return self.nombre

class Cuenta(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	domicilio = models.CharField('Domicilio de la Compania', max_length=255, null=True, blank=True)
	rif = models.CharField('Registro de Informacion Fiscal', max_length=255, null=True, blank=True)
	movil = models.CharField('Telefono Movil', max_length=8, null=True, blank=True)
	local = models.CharField('Telefono Fijo', max_length=8, null=True, blank=True)
	correo = models.EmailField('Correo Electronico', null=True, blank=True)
	pagina = models.URLField('Pagina Web', null=True, blank=True)
	sector = models.ForeignKey(Sectores, null=True, blank=True, on_delete=models.SET_NULL)

	class Meta:
		verbose_name = "Cuenta"
		verbose_name_plural = "Cuentas"

	def __str__(self):
		return self.rif

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cuenta.objects.create(usuario=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
 #   instance.cuenta.save()