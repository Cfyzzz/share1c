
from django.shortcuts import render, get_object_or_404
from cod.models import Cod


# Create your views here.
def detail(request, uid):
    record = get_object_or_404(Cod, uid=uid)

    return render(request, 'cod.html', {'record': record})
