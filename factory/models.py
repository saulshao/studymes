from django.db import models
from django.contrib.auth.models import User

#import base model
from mespublic.models import *

# Create your models here.

#Administrative region
class Region(Common, Rowtracking, Recurrence):

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'region'
        
#Company
class Company(Common, Rowtracking):

    def __str__ (self):
        return self.name
        
    class Meta:
        db_table = u'company'

#Department belong to company
class Department(Common, Rowtracking, Recurrence):
    company = models.ForeignKey(
                                Company, 
                                on_delete=models.PROTECT, 
                                null = True,
                                )

    #Link department to user                            
    employees = models.ManyToManyField(
                                        User,
                                        through='Employeeship',
                                        through_fields=('department', 'user'),
                                      )
                                      
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'department'

class Employeeship(models.Model):
    user = models.ForeignKey(
                                User, 
                                on_delete=models.PROTECT, 
                                null = True,
                            )
    department = models.ForeignKey(
                                    Department, 
                                    on_delete=models.PROTECT, 
                                    null = True,
                                  )
                                  
    class Meta:
        db_table = u'employeeship'
        
#Factory
class Factory(Common, Rowtracking):
    region = models.ForeignKey(
                             Region, 
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True, 
                             )
    company = models.ForeignKey(
                            Company, 
                            on_delete=models.PROTECT,
                            null = True,
                            )

    address = models.CharField(
                                max_length=2000, 
                                default='UNKNOWN'
                                )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'factory'

#Workshop in factory
class Workshop(Common, Rowtracking):
    factory = models.ForeignKey(
                                Factory, 
                                on_delete=models.PROTECT, 
                                null = True,)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'workshop'

#line in workshop
class Line(Common, Rowtracking):

    LINE_TYPE = (
        (1, 'Line'), #flow line
        (2, 'Cell'), #cell line
    )

    workshop = models.ForeignKey( Workshop, 
                                  on_delete=models.PROTECT, 
                                  null = True,
                                  )
    department = models.ForeignKey( Department, 
                                    on_delete=models.PROTECT, 
                                    null = True,
                                    )
    line_type = models.IntegerField(
                                    choices=LINE_TYPE,
                                    null = True,
                                    )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'line'

#station in line
class Station(Common, Rowtracking):
    line = models.ForeignKey(
                              Line, 
                              on_delete=models.PROTECT, 
                              null = True,
                            )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'station'
