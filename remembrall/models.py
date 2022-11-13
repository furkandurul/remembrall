from django.db import models
# Create your models here.

class Post(models.Model):
	description = models.TextField(default="NULL")
	tags = models.TextField(default="NULL")
	publish_date = models.DateTimeField("date created")
	creator = models.ForeignKey("auth.User", to_field="username", on_delete=models.CASCADE, default="unknown_user")
	content = models.TextField(default="NULL")
	ref_link = models.URLField(default="NULL")
	def __str__(self):
		return(
			f"description:{self.description}\n \
			tags:{self.tags}\n \
			publish_date:{self.publish_date}\n \
			creator:{self.creator}\n \
			content:{self.content}\n \
			ref_link:{self.ref_link}\n"
			)
