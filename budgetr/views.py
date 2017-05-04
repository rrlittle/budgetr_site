from django.shortcuts import render, get_object_or_404
from models import Flow
from forms import FlowPost
from datetime import datetime
import utils


def index(request):
    context = {
        'flows': [FlowPost(instance=f) for f in Flow.objects.all()]
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
