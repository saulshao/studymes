from django.db import models

# Create your models here.
#import base model
from mespublic.models import *

#nation or country
class Label(Common,Rowtracking):

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'label'

#City
class LabelTemplate(Common,Rowtracking):
    PRINTER_TYPE = (
      (1,'Barcode printer'),
      (2,'Laser printer'),
      )
    
    printer_type = models.IntegerField(
                                      choices = PRINTER_TYPE,
                                      null = True,
                                      )
    
    content = models.TextField(
        null = True,
        help_text = 'Template content'
    )    
    
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'label_template'


class LabelTemplateAssignRule(Rowtracking):

    label = models.ForeignKey(
                                Label, 
                                on_delete=models.PROTECT, 
                                null = True,
                            )
    label_template = models.ForeignKey(
                                    LabelTemplate, 
                                    on_delete=models.PROTECT, 
                                    null = True,
                                  )
    assignment_expression = models.TextField(
                        null = True,
                        help_text = 'Complicated boolean expression'
                        )
                                          
    class Meta:
        db_table = u'label_template_assign_rule'
            
class LabelVariable(Common,Rowtracking):
    VARIABLE_TYPE = () 
        
    assignment_expression = models.TextField(
                        null = True,
                        help_text = 'Complicated boolean expression'
                        )
                                          
    class Meta:
        db_table = u'label_variable'