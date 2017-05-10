from django.shortcuts import render, get_object_or_404
from models import Flow
from datetime import datetime
import utils

freq_types = [
    'Years',
    'Months',
    'Weeks',
    'Days'
]


def index(request):
    flows = []
    for f in Flow.objects.all():
        recurr = f.recurrence
        rules = []
        for rule in recurr.rrules:
            rrule = {
                'exclude': False,
                'id': id(rule),
                'freq': rule.freq,
                'weekdays': rule.byday,
                'months': rule.bymonth,
                'monthdays': rule.bymonthday,
                'label': rule.to_text(),
                'freq_type': freq_types[rule.freq]
            }
            rules.append(rrule)
        for rule in recurr.exrules:
            rrule = {
                'exclude': True,
                'id': id(rule),
                'freq': rule.freq,
                'weekdays': rule.byday,
                'months': rule.bymonth,
                'monthdays': rule.bymonthday,
                'label': rule.to_text(),
                'freq_type': freq_types[rule.freq]
            }
            rules.append(rrule)

        dates = [{'date': d.strftime('%m/%d/%Y'), 'exclude': False}
                 for d in recurr.rdates]
        dates += [{'date': d.strftime('%m/%d/%Y'), 'exclude': True}
                 for d in recurr.exdates]

        flow = {
            'id': f.id,
            'name': f.name,
            'start': f.start_date.strftime('%m/%d/%Y'),
            'rules': rules,
            'dates': dates,
        }
        flows.append(flow)
    context = {
        'flows': flows
    }
    
    return render(request, 'budgetr/index.html', context)


def getflows(request, htmljson):
    ''' returns json with all the existing flow modules as either html or json
        so you can embed them, directly into a div or populate your own form
    '''
    pass


def new_flow(request):
    ''' returns either the html for an empty flow form, this one has an
        editable title. until it is saved
    '''
    pass

def getflow(request, flowid):
    ''' returns the html for a single flow
    '''
    pass

# def flow(request, flowid, end_yr, end_mo, end_day):
#     end_date = datetime(int(end_yr), int(end_mo), int(end_day))
#     flow = get_object_or_404(Flow, flowid)
#     tally = utils.calc_flow(flow, end_date)
#     return utils.plot(tally)


# def wealth(request, end_yr, end_mo, end_day):
#     end_date = datetime(int(end_yr), int(end_mo), int(end_day))
#     print 'calcing wealth'
#     wealth = utils.calc_wealth(end_date)
#     print wealth
#     return utils.plot(wealth)
