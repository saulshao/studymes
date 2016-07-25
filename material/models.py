from django.db import models

# Create your models here.

#import base model
from mespublic.models import Common, Rowtracking
from factory.models import *

class MaterialCategory(Common, Rowtracking,Recurrence):
    enabled = models.BooleanField(
                                  default=True
                                 )

    class Meta:
        db_table = u'material_category'

class Material(Common, Rowtracking):         
    
    enabled = models.BooleanField(
            default=True
        )    
    belong_to = models.ManyToManyField(
        MaterialCategory,
        through='MaterialBelongtoCategory',
        through_fields=('material','material_category',),
    )    

    class Meta:
        db_table = u'material'
        
class MaterialBelongtoCategory(models.Model):
    material = models.ForeignKey(
                                Material, 
                                on_delete=models.PROTECT, 
                                null = True,
                            )
    material_category = models.ForeignKey(
                                    MaterialCategory, 
                                    on_delete=models.PROTECT, 
                                    null = True,
                                  )
                                  
    class Meta:
        db_table = u'material_category_r'