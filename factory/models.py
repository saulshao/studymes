from django.db import models

#import base model
from mespublic.models import MesCommon

# Create your models here.
class Nation(MesCommon):

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'nation'

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

class Company(MesCommon):
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'company'

class Department(MesCommon):
    company = models.ForeignKey(
                                Company, 
                                on_delete=models.PROTECT, 
                                default = 0)
  
    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'department'

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

class Workshop(MesCommon):
    factory = models.ForeignKey(
                                Factory, 
                                on_delete=models.PROTECT, 
                                default = 0)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'workshop'


class Line(MesCommon):
    LINE_TYPE = (
        (1, 'Line'),
        (2, 'Cell'),
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