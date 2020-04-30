from djongo import models

class JobsList(models.Model):
	jobTitle = models.CharField(max_length=100)
	jobDescription = models.TextField()
	jobUrl = models.URLField()
	createdTime = models.DateTimeField(auto_now_add=True,auto_now=False)