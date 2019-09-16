from django.shortcuts import render, get_object_or_404
from workshop_week.models import Workshop, User
from .forms import ProposeForm
# Create your views here.


def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        'workshops': workshops
    }
    return render(request, 'workshop_week/workshop_index.html', context)


def workshop_detail(request, id):
    try:
        workshop = Workshop.objects.get(pk=id)
        presenters = workshop.presenter.all()
    except Workshop.DoesNotExist:
        raise Http404("Workshop does not exist")
    return render(request, 'workshop_week/workshop_detail.html',
                  {'workshop': workshop, 'presenter': presenters})


def workshop_propose(request):
    if request.method == "POST":

    else:
        form = ProposeForm()
        return render(request, 'workshop_week/workshop_propose.html', {'form': form})
