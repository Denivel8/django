from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_lenght=128, unique=True)
    def__str__(self):
        return self.name
	
class Page(models.Model):
	category=models.ForeignKey(Category)
	title= models.CharField(max_lenght=128)
	url=models.URLField()
	views=models.IntegerField(dafault=0)
	def__str__(self):
	    return self.title
	
