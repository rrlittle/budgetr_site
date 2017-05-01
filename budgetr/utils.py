from datetime import timedelta, datetime
from models import Flow
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.http import HttpResponse


def dt_str(dt):
    return dt.strftime('%Y/%m/%d')


def strp(dt_str):
    return datetime.strptime(dt_str, '%Y/%m/%d')


def list_of_days(start_date, end_date):
    ''' lists all the days between start and end date in order
    '''
    day_count = (end_date - start_date).days + 1
    return [dt_str(d) for d in (start_date + timedelta(n)
                                for n in range(day_count))]


def calc_flow(flow, end_date):
    tally = []
    prev = flow.initial
    ocs = flow.recurrence.between(flow.start_date, end_date)
    ocs = [dt_str(d) for d in ocs]
    # import ipdb; ipdb.set_trace()
    for date in list_of_days(flow.start_date, end_date):
        if date in ocs:
            prev += flow.amount
        tally.append({'date': date, 'value': prev})
    return tally


def calc_wealth(end_date):
    wealth = {}
    for flow in Flow.objects.all():
        tally = calc_flow(flow, end_date)
        for entry in tally:
            if not entry['date'] in  wealth:
                wealth[entry['date']] = 0
            wealth[entry['date']] += entry['value']
    return [{'date': k, 'value': wealth[k]} for k in sorted(wealth.keys())]


def plot(flow_data):
    y = []
    x = []
    [(y.append(d['value']), x.append(strp(d['date']))) for d in flow_data]
    fig = Figure()
    ax = fig.add_subplot(111)
    print '++++++++++++++'
    ax.plot_date(x, y, '-')
    print '--------------'
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response