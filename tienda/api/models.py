from django.db import models
from django.urls import reverse


class Stock_En_Tienda(models.Model):

    id_tienda = models.CharField(max_length=30, default=None, null=True)
    id_producto = models.CharField(max_length=30, default=None, null=True)
    categoria = models.ForeignKey(
        "api.categoria", on_delete=models.CASCADE, null=True)
    sku = models.CharField(max_length=30, default=None, null=True)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    tiene_iva = models.BooleanField()
    estado = models.CharField(max_length=30)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    margen_ganancia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Tienda(models.Model):

    id_ciudad = models.CharField(max_length=100)
    logo = models.FileField(null=True, upload_to="upload/tienda/")
    nombre = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Categoria(models.Model):

    icono = models.FileField(null=True, upload_to="upload/categoria/")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class SubCategoria(models.Model):

    # Relationships
    categoria = models.ForeignKey("api.categoria", on_delete=models.PROTECT)

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=100)
    icono = models.FileField(null=True, upload_to="upload/subcategoria/")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Producto(models.Model):

    nombre = models.CharField(max_length=255)
    presentacion = models.TextField(max_length=100)
    marca = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    foto = models.FileField(null=True, upload_to="upload/productos/")
    venta_al_granel = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=100)
    nivel_azucar = models.CharField(max_length=10)
    nivel_sal = models.CharField(max_length=30)
    nivel_grasa = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
