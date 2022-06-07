from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models

# Create your models here.
#tabla 1
class proveedor(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True, null=False, blank=False)
    cuit=models.CharField(max_length=11, null=False)
    direccion=models.CharField(max_length=50, null=False)
    email=models.EmailField(null=True)
    telefono=models.CharField(max_length=7, null=True)

    def __str__(self):
        txt = "{0} ({1}) / {2}"
        return txt.format(self.nombre, self.cuit, self.direccion)

#tabla 3
class producto(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True, null=False, blank=False)
    marca=models.CharField(max_length=30, null=False)
    costo=models.FloatField(null=False)
    precio=models.FloatField(null=False)
    categoria=models.CharField(max_length=30)
    UnidadMedida=models.CharField(max_length=20)
    peso=models.IntegerField()

    def __str__(self):
        txt = "{0} ({1}) / Costo: {2} / Precio: {3}"
        return txt.format(self.nombre, self.marca, self.costo, self.precio)

#tabla 2 foreignkey de producto
class deposito(models.Model):
    productos=models.ForeignKey(producto, blank=True, null=True, on_delete=models.CASCADE)
    cant=models.IntegerField(null=False)
    codigoDeBarra=models.IntegerField(null=False)
    stockMin=models.IntegerField()

    def __str__(self):
        txt = "{0} ({1}) / Codigo de barras: {2}"
        return txt.format(self.productos, self.cant, self.codigoDeBarra)

#tabla 4 foreignkey proveedores y producto
class compra(models.Model):
    id=models.CharField(max_length=50, primary_key=True, null=False)
    proveedores=models.ForeignKey(proveedor, null=True, blank=True, on_delete=models.CASCADE)
    productos=models.ForeignKey(producto, blank=True, null=True, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now_add=True)
    totalCompra=models.FloatField()

    def __str__(self):
        txt = "{0} ({1}) / ({2})"
        return txt.format(self.registro, self.proveedores, self.productos)

#tabla 6
class cliente(models.Model):
    dni=models.IntegerField(primary_key=True, null=False, blank=False)
    nombre=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField()
    domicilio=models.CharField(max_length=50)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.nombre, self.dni)

#tabla 5 foreign key producto y clientes
class venta(models.Model):
    factura=models.CharField(max_length=10, primary_key=True)
    clientes=models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE)
    productos=models.ForeignKey(producto, null=True, blank=False, on_delete=models.CASCADE)
    importeTotal=models.FloatField()
    fecha=models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "{0} ({1}) / {2}"
        return txt.format(self.factura, self.clientes, self.productos)
