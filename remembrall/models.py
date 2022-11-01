from django.db import models

# Create your models here.

class Post(models.Model):
	post_id = models.CharField(max_length=200, default="0")
	ref_link = models.URLField()
	publish_date = models.DateTimeField("date created")
	creator_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, to_field="user_id")

	def __str__(self):
		return(
			f"post_id:{self.post_id}\n \
			ref_link:{self.ref_link}\n \
			publish_date:{self.publish_date}\n \
			creator_id:{self.creator_id}\n"
			)

class User(models.Model):
	user_id = models.CharField(max_length=200, unique=True, default="0")
	user_name = models.CharField(max_length=50, default="new_user")
	user_email = models.URLField()
	sign_up_date = models.DateField("date registered")

	def __str__(self):
		return(
			f"user_id:{self.user_id}\n \
			user_name:{self.user_name}\n \
			user_email:{self.user_email}\n \
			sign_up_date:{self.sign_up_date}" 
			)