from django.db import models
import datetime
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	answer = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = "Published Recently ?"

@receiver(pre_save, sender=Question)
def demo_pre_save(sender, **kwargs):
	print("this function will be called before question is actually saved")

@receiver(post_save, sender=Question)
def demo_post_save(sender, **kwargs):
	print("this signal will be called after saving the model")

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
