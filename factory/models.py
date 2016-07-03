from django.db import models
#import datetime

# Create your models here.
class MesCommon(models.Model):
    code = models.CharField(
                            max_length=20, 
                            unique = True, 
                            help_text = 'Computer readable name'
                            )
    short_name = models.CharField(
                            max_length=20, 
                            default='Unknown',
                            help_text = 'Human readable abbr name'
                            )                        
    name = models.CharField(
                            max_length=200, 
                            help_text = 'Human readable name'
                            )
    desc = models.TextField(
                            null = True,
                            help_text = 'Long description, full name'
                            )
    created_time_stamp = models.DateTimeField(
                                                auto_now_add=True,
                                                null=True,
                                                help_text='Create time stamp',
                                                editable=False
                                            ) 
    created_by = models.CharField(
                                    max_length=20,
                                    default='system',
                                    help_text='User account who creates the row',
                                    editable=False
                                )
    updated_time_stamp = models.DateTimeField(
                                                auto_now=True,
                                                null=True,
                                                help_text='Update time stamp',
                                                editable=False
                                ) 
    updated_by = models.CharField(
                                    max_length=20,
                                    default='system',
                                    help_text='User account who updates the row',
                                    editable=False
                                )
    class Meta:
        abstract = True
        ordering = ['code','name']

class Nation(MesCommon):
    #created_date = models.DateTimeField('date created', default = datetime.utc())

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
    line = models.ForeignKey(Line, on_delete=models.PROTECT, default = 0)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'station'