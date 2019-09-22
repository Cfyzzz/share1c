
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from new.forms import ViewCodeForm
from cod.models import Cod


# Create your views here.
def detail(request, pk):
    record = get_object_or_404(Cod, pk=pk)

    return render(request, 'cod.html', {'record': record})
