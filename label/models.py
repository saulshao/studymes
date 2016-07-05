from django.db import models

# Create your models here.
#import base model
from mespublic.models import MesCommon

#nation or country
class Label(MesCommon):

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'label'

#City
class LabelTemplate(MesCommon):
    TPL_FORMAT = (
      (1,'Barcode printer'),
      (2,'Laser printer'),
      )
    
    format_type = models.IntegerField(
                                      choices = TPL_FORMAT
                                      default = 1
                                      )
    
    url = models.
    
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'label_template'
