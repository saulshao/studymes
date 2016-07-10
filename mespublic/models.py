from django.db import models

# Create your models here.

#basic mes object definition which has some shared attributes.
class Common(models.Model):
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

    def __str__ (self):
        return self.name
        
    class Meta:
        abstract = True
        ordering = ['code','name']

class Rowtracking(models.Model):
    created_time_stamp = models.DateTimeField(
                                                auto_now_add=True,
                                                null=True,
                                                help_text='Created time stamp',
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
                                                help_text='Updated time stamp',
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

class Recurrence(models.Model):
    parent = models.ForeignKey(
                                 'self', 
                                 null = True,
                                 blank = True,
                                 default = None,
                                 related_name="children",
                                )
                                
    class Meta:
        abstract = True


