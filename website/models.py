from django.db import models

#The database model

class Record(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	company=models.CharField(max_length=20, default='ROSSI')
	position=models.CharField(max_length=50)
	created_at=models.DateTimeField(auto_now_add=True)
	note=models.CharField(max_length=100, blank=True)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")