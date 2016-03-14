from django.shortcuts import render
from django.db.models import Count

from mqm_base.models import Locale

def index(request):
    locales = (Locale.objects
        .order_by('name')
        .annotate(issues_count=Count('issues')))
    return render(request, 'framework/index.html', {
        "locales": locales
    })
