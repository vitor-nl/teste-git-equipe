from django.db import models

# Create your models here.

class Pig(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Porco'
        verbose_name_plural = 'Porcos'
        ordering =['id']

    def __str__(self):
        return self.name