from django.db import models

class Frog(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Frog'
        verbose_name_plural = 'Frogs'
        ordering =['id']

    def __str__(self):
        return self.name

