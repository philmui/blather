from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blat(models.Model):
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)
	created_by = models.ForeignKey(User)

	def total_likes(self):
		return self.like_set.count()

	def __unicode__(self):
		return self.text[:50] + ":" + str(self.created_by)

class Like(models.Model):
	blat = models.ForeignKey(Blat, 
				on_delete=models.CASCADE)

class Profile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(blank=True)
	blog = models.TextField(blank=True)
	
