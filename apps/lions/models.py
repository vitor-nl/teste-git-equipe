from django.db import models

# Create your models here.
class Lion(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Lion'
        verbose_name_plural = 'Lions'
        ordering =['id']

    def __str__(self):
        return self.name
