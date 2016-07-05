from django.db import models
from django.contrib.auth.models import User

#import base model
from mespublic.models import *

# Create your models here.

#nation or country
class Nation(MesCommon):

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'nation'

#City
class City(MesCommon):
    nation = models.ForeignKey(
                                Nation, 
                                on_delete=models.PROTECT, 
                                default = 0
                                )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'city'

#Company
class Company(MesCommon):
    def __str__ (self):
        return self.name
        
    class Meta:
        db_table = u'company'

#Department belong to company
class Department(MesCommon):
    company = models.ForeignKey(
                                Company, 
                                on_delete=models.PROTECT, 
                                default = 0
                                )
    parent_department = ForeignKey(
                                    'self', 
                                    on_delete=models.PROTECT, 
                                    default = 1
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
                                default = 0
                            )
    department = models.ForeignKey(
                                    Department, 
                                    on_delete=models.PROTECT, 
                                    default = 0
                                  )
                                  
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'employeeship'
        
#Factory
class Factory(MesCommon):
    city = models.ForeignKey(
                             City, 
                             on_delete=models.PROTECT, 
                             default = 0
                             )
    company = models.ForeignKey(
                            Company, 
                            on_delete=models.PROTECT,
                            default = 0
                            )

    address = models.CharField(
                                max_length=2000, 
                                default='Unknown'
                                )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'factory'

#Workshop in factory
class Workshop(MesCommon):
    factory = models.ForeignKey(
                                Factory, 
                                on_delete=models.PROTECT, 
                                default = 0)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'workshop'

#line in workshop
class Line(MesCommon):

    LINE_TYPE = (
        (1, 'Line'), #flow line
        (2, 'Cell'), #cell line
    )

    workshop = models.ForeignKey( Workshop, 
                                  on_delete=models.PROTECT, 
                                  default = 0
                                  )
    department = models.ForeignKey( Department, 
                                    on_delete=models.PROTECT, 
                                    default = 0
                                    )
    line_type = models.IntegerField(
                                    choices=LINE_TYPE,
                                    default = 1
                                    )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'line'

#station in line
class Station(MesCommon):
    line = models.ForeignKey(
                              Line, 
                              on_delete=models.PROTECT, 
                              default = 0
                            )

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'station'
