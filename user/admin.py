from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    pass


class RoleAdmin(admin.ModelAdmin):
    pass

class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Usuario, UsuarioAdmin)
