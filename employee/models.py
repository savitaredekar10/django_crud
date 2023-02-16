from django.db import models

class Info(models.Model):
	name=models.CharField(max_length=40)
	uid=models.IntegerField()
	email=models.EmailField(max_length=50)
	gender=models.CharField(max_length=10)
	location=models.CharField(max_length=20)
	country=models.CharField(max_length=20)

	def _str_(self):
		return self.name 
