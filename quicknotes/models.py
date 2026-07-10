from django.db import models

class Note(models.Model):
    name = models.TextField()
    content= models.TextField()

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()    
    
