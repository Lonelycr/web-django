from django.db import models


class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'deporte'

class Infraestructura(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('mantenimiento', 'En Mantenimiento'),
        ('inactivo', 'Inactivo'),
        ('reparacion', 'En Reparación'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, default='default_value')
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    horarios = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    foto = models.ImageField(upload_to='infraestructuras/', blank=True, null=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='activo'
    )
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE, related_name='infraestructuras')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'infraestructura'

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_usuario'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    clave = models.CharField(max_length=45)
    tipo_usuario = models.ForeignKey(
        'TipoUsuario', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='usuarios'
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'usuario'


class Reserva(models.Model):
    infraestructura = models.ForeignKey(Infraestructura, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario = models.TimeField()
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'reserva'
