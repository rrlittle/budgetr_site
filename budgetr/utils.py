from datetime import timedelta


def list_of_days(start_date, end_date):
	''' lists all the days between start and end date in order
	'''
	day_count = (end_date - start_date).days + 1
	return [d for d in (start_date + timedelta(n) for n in range(day_count))]


def datetime_in_datetime_list(dt, dtl):
	for dti in dtl:
		if dti.year == dt.year and dti.month == dt.month and dti.day == dt.day:
			return True
	return False
