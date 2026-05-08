from django.db import models


class Plato(models.Model):
    CATEGORIAS = [
        ('Entrada', 'Entrada'),
        ('Fondo', 'Fondo'),
        ('Bebida', 'Bebida'),
        ('Postre', 'Postre'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre
 

class Pedido(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Preparando', 'Preparando'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='Pendiente')
    platos = models.ManyToManyField(Plato, related_name='pedidos')

    def __str__(self):
        return f'Pedido #{self.id} - {self.estado}'