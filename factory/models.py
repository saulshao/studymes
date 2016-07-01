from django.db import models

# Create your models here.
class Nation(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'nation'

class City(models.Model):
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'city'

class Company(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'company'

class Factory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE,  default = 0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    address = models.CharField(max_length=2000,default='Unknown')

    class Meta:
        db_table = u'factory'

class Workshop(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'workshop'

class Line(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'line'

class Station(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE, default = 0)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'station'