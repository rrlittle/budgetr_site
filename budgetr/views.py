from django.shortcuts import render, get_object_or_404
from models import Flow
from forms import FlowPost
from datetime import datetime
import utils


def index(request):
    flowsForms = []
    for f in Flow.objects.all():
        fp = FlowPost(instance=f)
        fpv = fp.visible_fields()
        flowsForms.append({
            'name': fpv[0], 
            'recurrence': fpv[1].as_widget(attrs={
                'id': '%s-%s' % (f, f.id),
                'class': 'recurrence-widget'
            })
        })
    context = {
        'flows': flowsForms
    }
    
    return render(request, 'budgetr/index.html', context)


def flow(request, flowid, end_yr, end_mo, end_day):
    end_date = datetime(int(end_yr), int(end_mo), int(end_day))
    flow = get_object_or_404(Flow, flowid)
    tally = utils.calc_flow(flow, end_date)
    return utils.plot(tally)


def wealth(request, end_yr, end_mo, end_day):
    end_date = datetime(int(end_yr), int(end_mo), int(end_day))
    print 'calcing wealth'
    wealth = utils.calc_wealth(end_date)
    print wealth
    return utils.plot(wealth)
