from django.db import models

# Create your models here.
class Program(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    number_semesters = models.SmallIntegerField(default=1)
    is_active = models.BooleanField(default = True)                                          
    def __str__(self):
        return self.name
    class Meta:  
        db_table = 'Program'


class Pensum(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, unique=True)
    program_code = models.ForeignKey(Program, on_delete= models.CASCADE)
    file_pdf = models.FileField(upload_to= 'pensum', null = False)
    expiration_date = models.DateField(auto_now =False, auto_now_add=False)
    date_issue = models.DateField(auto_now =False, auto_now_add=False)
    is_active = models.BooleanField(default = True)                                            
    def __str__(self):
        return str(self.code)
    class Meta:  
        db_table = 'Pensum'