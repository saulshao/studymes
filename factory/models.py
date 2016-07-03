from django.db import models
#import datetime

# Create your models here.
class Nation(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)
    #created_date = models.DateTimeField('date created', default = datetime.utc())

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'nation'

class City(models.Model):
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'city'

class Company(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'company'

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'department'

class Factory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE,  default = 0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=2000,default='Unknown')

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'factory'

class Workshop(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'workshop'


class Line(models.Model):
    LINE_TYPE = (
        (1, 'Line'),
        (2, 'Cell'),
    )
    workshop = models.ForeignKey(Workshop, 
                                 on_delete=models.CASCADE, 
                                 default = 0)
    department = models.ForeignKey( Department, 
                                    on_delete=models.CASCADE, 
                                    default = 0)
    line_type = models.IntegerField(
                                    choices=LINE_TYPE,
                                    default=1,)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'line'

class Station(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        db_table = u'station'