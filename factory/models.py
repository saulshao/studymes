from django.db import models

# Create your models here.
class Nation(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'nation'

class City(models.Model):
    models.ForeignKey(Nation, on_delete=models.CASCADE)
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
    models.ForeignKey(City, on_delete=models.CASCADE)
    models.ForeignKey(Company, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'factory'

class Workshop(models.Model):
    models.ForeignKey(Factory, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'workshop'

class Line(models.Model):
    models.ForeignKey(Workshop, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)

    class Meta:
        db_table = u'line'