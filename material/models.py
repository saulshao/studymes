from django.db import models

# Create your models here.

#import base model
from mespublic.models import MesCommon
from factory.models import *

class MaterialCategory(MesCommon):
    factory = models.ForeignKey(
                                Factory, 
                                on_delete=models.PROTECT, 
                                default = 0
                                )

    parent_material_category = models.ForeignKey(
                                                    'self', 
                                                    on_delete=models.PROTECT, 
                                                    default = 0
                                                )

    enabled = models.BooleanField(
                                  default=True
                                 )
    

    class Meta:
        db_table = u'material_category'

class Material(MesCommon):

    factory = models.ForeignKey(
                                Factory, 
                                on_delete=models.PROTECT, 
                                default = 0
                                )
    material_category = models.ForeignKey(
                                            MaterialCategory, 
                                            on_delete=models.PROTECT, 
                                            default = 0
                                         )
    enabled = models.BooleanField(
                                  default=True
                                 )
    

    class Meta:
        db_table = u'material'