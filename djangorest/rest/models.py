from django.db import models

# # Create your models here.
class Post(models.Model):
   title = models.CharField( max_length = 200)  
   content = models.TextField() 
   draft = models.BooleanField(default = False) 
   read_time = models.IntegerField(default = 0) 
   updated = models.DateTimeField( auto_now=True, auto_now_add=False)
   created = models.DateTimeField( auto_now=False, auto_now_add=True)

   class Meta:
       ordering = ["-created","-updated"]
    

   def __str__(self):
       return self.title 
    