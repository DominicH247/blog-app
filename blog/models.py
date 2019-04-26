from django.db import models


class Post(models.Model):
	"""Post models for the blog"""
	title = models.CharField(max_length=200)  # max character length fot title 200 characters
	author = models.ForeignKey(
			'auth.user',
			on_delete = models.CASCADE,  # for all many to one relationships must specify on_delete option. 
		)
	body = models.TextField()
	#post_date = models.DateField()

	def __str__(self):
		"""string representation of post model title"""
		return self.title
