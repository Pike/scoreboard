from django.shortcuts import render, get_object_or_404

from mqm_base.models import Locale, Issue

def locale_issues(request, locale_code):
    locale = get_object_or_404(Locale, code=locale_code)
    issues = (Issue.objects
        .filter(locale=locale))[:100]
    return render(request, 'mqm_base/locale-issues.html', {
        "locale": locale,
        "issues": issues
    })
