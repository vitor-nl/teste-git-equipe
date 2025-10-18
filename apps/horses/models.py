from django.db import models

# Create your models here.
class Horse(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Cavalo'
        verbose_name_plural = 'Cavalos'
        ordering =['id']

    def __str__(self):
        return self.name