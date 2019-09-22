from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AddCodeForm
from cod.models import Cod


# Create your views here.
def index(request):
    if request.method == 'POST':
        if "_new_record" in request.POST:
            form = AddCodeForm(request.POST)

            if form.is_valid():
                new_record = Cod(row_code=form.cleaned_data['row_code'])
                new_record.save()
                return HttpResponseRedirect('/cod/' + str(new_record.pk))

    form = AddCodeForm(initial={'row_code': ""})
    context = {'form': form}
    return render(request, 'new_code.html', context)

