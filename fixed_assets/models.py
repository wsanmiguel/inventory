from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DocumentType(models.Model):
    '''Tipo de Documento'''
    id = models.CharField('ID', max_length=2, primary_key=True)
    name = models.CharField('Nombre', max_length=80)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"


class Third(models.Model):
    '''Terceros'''
    identification = models.CharField(
        'Identificación', max_length=20, primary_key=True)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.RESTRICT)
    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField(
        'Apellidos', max_length=100, null=True, blank=True)
    phone = models.CharField('Teléfono', max_length=50, null=True, blank=True)
    address = models.CharField(
        'Dirección', max_length=200, null=True, blank=True)
    birthday = models.DateField('Fecha de Nacimiento', null=True, blank=True)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "Tercero"
        verbose_name_plural = "Terceros"


class Patient(models.Model):
    '''Paciente'''

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Supplier(models.Model):
    '''Proveedor'''

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"


class Position(models.Model):
    '''Cargo de Colaborador'''
    name = models.CharField('Nombre', max_length=200)
    code = models.CharField('Código', max_length=50, null=True, blank=True)
    active = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class CostCenter(models.Model):
    '''Centro de Costos'''
    name = models.CharField('Nombre', max_length=200)
    code = models.CharField('Código', max_length=200)
    active = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = "Centro de Costos"
        verbose_name_plural = "Centros de Costos"


class Sectional(models.Model):
    '''Seccional'''
    name = models.CharField('Nombre', max_length=200)
    address = models.CharField(
        'Dirección', max_length=250, null=True, blank=True)
    pattern_inventory = models.CharField(
        'Patrón de Inventario', max_length=30, null=True, blank=True)
    active = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = "Seccional"
        verbose_name_plural = "Seccionales"


class Collaborator(Third):
    '''Colaborador'''
    position = models.ForeignKey(
        Position, on_delete=models.RESTRICT, null=True, blank=True)
    cost_center = models.ForeignKey(
        CostCenter, on_delete=models.RESTRICT, null=True, blank=True)
    sectional = models.ForeignKey(
        Sectional, on_delete=models.RESTRICT, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"


class Building(models.Model):
    '''Edificio de Seccional'''
    name = models.CharField(max_length=200)
    sectional = models.ForeignKey(Sectional, on_delete=models.RESTRICT)
    address = models.CharField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"


class Flat(models.Model):
    '''Planta-Piso del Edificio'''
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Planta de Edificio"
        verbose_name_plural = "Plantas de Edificio"


class Space(models.Model):
    '''Espacio en el Piso del Edificio'''
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Espacio de Piso"
        verbose_name_plural = "Espacios de Piso"


class Warehouse(models.Model):
    '''Bodega'''
    description = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)
    flat = models.ForeignKey(
        Flat, on_delete=models.RESTRICT, null=True, blank=True)
    space = models.ForeignKey(
        Space, on_delete=models.RESTRICT, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"


class Maker(models.Model):
    name = models.CharField('Nombre', max_length=200)
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"


class AssetType(models.Model):
    name = models.CharField(max_length=250)
    inventory = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo de Activos"
        verbose_name_plural = "Tipos de Activos"


class Asset(models.Model):
    STATUS_CHOICE = (
        ('A', 'Activo'),
        ('N', 'Anulado'),
        ('R', 'Reparación'),
        ('P', 'Prestado'),
        ('B', 'Baja'),
    )
    description = models.CharField(max_length=255)
    serial = models.CharField(max_length=150, null=True, blank=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.RESTRICT, null=True, blank=True)
    asset_type = models.ForeignKey(AssetType, on_delete=models.RESTRICT)
    inventory = models.CharField(max_length=150, null=True, blank=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='A')

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"


class AssetField(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Campo de Activo"
        verbose_name_plural = "Campos de Activos"


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Traslado"
        verbose_name_plural = "Traslados"


class TransferField(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.RESTRICT)
    field = models.ForeignKey(AssetField, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Campo de Traslado"
        verbose_name_plural = "Campos de Traslados"


class TransferDetail(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.RESTRICT)
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    asset_field = models.ForeignKey(
        AssetField, on_delete=models.RESTRICT, null=True, blank=True)
    value = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Detalle de Traslado"
        verbose_name_plural = "Detalle de Traslados"


class Drop(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Baja"
        verbose_name_plural = "Bajas"


class DropDetail(models.Model):
    drop = models.ForeignKey(Drop, on_delete=models.RESTRICT)
    asset = models.ForeignKey(Asset, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Detalle de Baja"
        verbose_name_plural = "Detalle de Bajas"
