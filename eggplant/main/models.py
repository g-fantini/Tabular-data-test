from django.db import models

#Creating a Person model rather than customising the User one, 
#since no authentication is mentioned or mentioned

class Person(models.Model):
    """A class used to represent a Person
    """
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    #n_of_childs in the future could be  calculated by counting 
    #the 1:N relationships with other persons
    n_of_childs = models.PositiveIntegerField()
    