from __future__ import unicode_literals

from django.db import models
from recurrence.fields import RecurrenceField


class Flow(models.Model):
	name = models.CharField(max_length=20)
	memo = models.CharField(max_length=200, null=True, blank=True)
	initial = models.FloatField(default=0)
	start_date = models.DateTimeField()
	amount = models.FloatField()
	recurrence = RecurrenceField()
	goal = models.FloatField(blank=True, null=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
