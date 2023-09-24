from django.db import models

# Table containing the users
class Record(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	company=models.CharField(max_length=20, default='ROSSI')
	position=models.CharField(max_length=50)
	created_at=models.DateTimeField(auto_now_add=True)
	note=models.CharField(max_length=100, blank=True)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

#Table containing the equipent
class Equipment(models.Model):

	companies = (
		('rossi', 'Rossi Biofuel Zrt.'),
		('enviral', 'Enviral a.s.')
		)

	record = models.ForeignKey(Record, on_delete=models.CASCADE)
	hwtype = models.CharField(max_length=50)
	vendor = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	stag = models.CharField(max_length=50, blank=True)
	location = models.CharField(max_length=50, blank=True)
	status = models.CharField(max_length=50)
	pdate = models.DateTimeField(max_length=50, blank=True, null=True) #Date of purchase
	name = models.CharField(max_length=50, blank=True)
	licence = models.CharField(max_length=50, blank=True)
	rdate = models.DateTimeField(auto_now_add=True) # Date of registration
	company = models.CharField(max_length=50, choices=companies, default='rossi')

	def __str__(self):
		return(f"{self.id}")