from django.db import models
from categories.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    price = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('estoque', 'Em estoque'),
        ('esgotado', 'Esgotado'),
        ('solicitado', 'Solicitado'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name
    