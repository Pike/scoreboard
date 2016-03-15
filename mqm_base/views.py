from django.apps import apps as django_apps
from django.shortcuts import render, get_object_or_404

from mqm_base.models import Locale, Issue

import codecs
import os

def locale_issues(request, locale_code):
    locale = get_object_or_404(Locale, code=locale_code)
    issues = (Issue.objects
        .filter(locale=locale))[:100]
    scorecard = django_apps.get_app_config('mqm_tree_card')
    return render(request, 'mqm_base/locale-issues.html', {
        "locale": locale,
        "issues": issues,
        "scorecard": scorecard
    })

def issues_js(request):
    data = os.path.join(os.path.dirname(__file__), 'data')
    issues_xml = codecs.open(os.path.join(data, 'issues.xml'), encoding='utf-8').read()
    moz_issues_xml = codecs.open(os.path.join(data, 'moz-issues.xml'), encoding='utf-8').read()
    return render(request, 'mqm_base/issues.js', {
        "issues_xml": issues_xml,
        "moz_issues_xml": moz_issues_xml
    })
