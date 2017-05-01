from __future__ import unicode_literals

from django.db import models
from recurrence.fields import RecurrenceField


class Flow(models.Model):
	name = models.CharField(max_length=20)
	memo = models.CharField(max_length=200, null=True, blank=True)
	start_date = models.DateTimeField()
	amount = models.FloatField()
	recurrence = RecurrenceField()

	def __str__(self):
		return self.name
