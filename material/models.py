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

    material_category = models.ForeignKey(
                                            MaterialCategory, 
                                            on_delete=models.PROTECT, 
                                            default = 1
                                         )
                                         
    enabled = models.BooleanField(
                                  default=True
                                 )
    

    class Meta:
        db_table = u'material'