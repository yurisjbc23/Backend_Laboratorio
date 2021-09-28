from django.contrib import admin
from .models import *

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    pass


class PensumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Program, ProgramAdmin)
admin.site.register(Pensum, PensumAdmin)