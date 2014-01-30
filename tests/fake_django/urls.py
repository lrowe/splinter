import sys

from django.conf.urls import patterns, include, url
from django.http import HttpResponse

from django.contrib import admin
from django.contrib.auth.decorators import login_required
admin.autodiscover()

sys.path.append('tests')
from fake_webapp import EXAMPLE_HTML, EXAMPLE_IFRAME_HTML, EXAMPLE_ALERT_HTML, EXAMPLE_TYPE_HTML, EXAMPLE_NO_BODY_HTML, EXAMPLE_POPUP_HTML


def index(request):
    return HttpResponse(EXAMPLE_HTML)


def iframed(request):
    return HttpResponse(EXAMPLE_IFRAME_HTML)


def alertd(request):
    return HttpResponse(EXAMPLE_ALERT_HTML)


def type(request):
    return HttpResponse(EXAMPLE_TYPE_HTML)


def no_body(request):
    return HttpResponse(EXAMPLE_NO_BODY_HTML)


def get_name(request):
    return HttpResponse("My name is: Master Splinter")


def get_user_agent(request):
    return HttpResponse(request.user_agent.string)


def upload_file(request):
    if request.method == 'POST':
        f = request.FILES['file']
        buffer = []
        buffer.append("Content-type: %s" % f.content_type)
        buffer.append("File content: %s" % f.read())

        return HttpResponse('|'.join(buffer))


def foo(request):
    return HttpResponse("BAR!")


def query_string(request):
    if request.query_string == "model":
        return HttpResponse("query string is valid")
    else:
        raise Exception('500')


def popup(request):
    return HttpResponse(EXAMPLE_POPUP_HTML)


@login_required
def auth_required(request):
    return HttpResponse("Success!")


urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^iframe$', iframed),
    url(r'^alert$', alertd),
    url(r'^type$', type),
    url(r'^no_body$', no_body),
    url(r'^name$', get_name),
    url(r'^user_agent$', get_user_agent),
    url(r'^upload$', upload_file),
    url(r'^foo$', foo),
    url(r'^query$', query_string),
    url(r'^popup$', popup),
    url(r'^authenticate$', auth_required),
    url(r'^admin/', include(admin.site.urls)),
)
