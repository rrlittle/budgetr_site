from django.shortcuts import render
from models import Flow
from datetime import datetime
from utils import list_of_days, datetime_in_datetime_list


def index(request, end_yr, end_mo, end_day):
	end_date = datetime(int(end_yr), int(end_mo), int(end_day))
	ret = {}
	for flow in Flow.objects.all():
		prev = 0
		ret[flow.name] = []
		ocs = flow.recurrence.between(flow.start_date, end_date)
		for d in list_of_days(flow.start_date, end_date):
			if datetime_in_datetime_list(d, ocs):
				# import ipdb; ipdb.set_trace()
				prev += flow.amount
			ret[flow.name].append({
				'date': '%s/%s/%s' % (d.year, d.month, d.day),
				'value': prev
			})
	return render(request, 'budgetr/index.html', {'flows': ret})
