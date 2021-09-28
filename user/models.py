from django.db import models

# Create your models here.
from proyecto.models import *
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(models.Model):
    """Modelo Employee"""
    code = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    program_code = models.ForeignKey(Program, on_delete=models.CASCADE, default=0)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    Photo = models.ImageField(
        upload_to='pictures',
        default='pictures/default.jpg',
        max_length=255
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:  # pylint: disable=too-few-public-methods
        """Propiedades adicionales del modelo Employee"""
        db_table = 'Employee'

class Role(models.Model):
    """Modelo Role de Usuario"""
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:  # pylint: disable=too-few-public-methods
        """Propiedades adicionales del modelo Role"""
        db_table = 'Role'

class Usuario(models.Model):
    """ Modelo Usuario """
    code = models.AutoField(primary_key=True)
    username = models.EmailField(('Correo electronico'), unique=True)
    password=models.CharField(max_length= 20, blank= False, null= False)
    #first_name = None
    #last_name = None
    #is_staff = None
    #is_superuser = None
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

    class Meta:  # pylint: disable=too-few-public-methods
        """Propiedades adicioneles del modelo User"""
        db_table = 'Usuario'
