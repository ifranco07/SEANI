from django.db import models

# Create your models here.
class Stage (models.Model):
    stage= models.IntegerField(
        verbose_name= 'Etapa'
    )
    applicayion_date= models.DateField(
        verbose_name= 'Fecha de Aplicación'
    )
    
    @property
    def year(self):
        return self.application_date.year

    @property
    def month(self):
     months = ['enero', 'febrero', 'marzo','abirl', 'mayo', 'junio',
               'julio', 'agosto', 'septiembre','octubre', 'noviembre', 'diciembre',]
     return months[self.application_date.month - 1]

    def __str__(self):
        return f"{self.stage} - {self.month}{self.year}"

    class Meta: 
        verbose_name = 'etapa'
        verbose_name_plural = 'etapas'

