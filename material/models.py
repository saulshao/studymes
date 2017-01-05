from django.db import models

# Create your models here.

#import base model
from mespublic.models import Common, Rowtracking, Recurrence
#from factory.models import *

class MaterialCategory(Common, Rowtracking, Recurrence):
    """
        material category
    """
    enable = models.BooleanField(
        default=True
    )
    material_code_prefix = models.CharField(
        max_length=2000,
        help_text='Regular expression for part numebr',
    )

    class Meta:
        db_table = u'material_category'

class Material(Common, Rowtracking):
    """
        material master data
    """
    enable = models.BooleanField(
        default=True
    )
    belong_to = models.ManyToManyField(
        MaterialCategory,
        through='MaterialBelongtoCategory',
        through_fields=('material', 'material_category'),
    )

    class Meta:
        db_table = u'material'

class MaterialBelongtoCategory(models.Model):
    """
        material category v.s. material relationship
    """
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        null=True,
    )
    material_category = models.ForeignKey(
        MaterialCategory,
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        db_table = u'material_category_r'
