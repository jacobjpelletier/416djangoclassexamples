from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    '''
    textfield vs charfield: charfield allows you to restrict length, whereas textfield is a large dedicated space
    
    '''

    def __str__(self):
        # this generates a string with first name space last name by using f-string which is used for string
        # concatenation
        return f"{self.first_name} {self.last_name}"
