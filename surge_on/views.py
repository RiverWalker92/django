from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from management.models import Layout, Content, SmallContent, TeamMember

#from django.http import Http404
from django.shortcuts import render



def index(request):
    WebsiteName = Layout.objects.get(title="WebsiteName")
    SubTitle = Layout.objects.get(title="SubTitle")
    Features = Content.objects.get(title_id="features")
    TeamMember1 = TeamMember.objects.get(pk=1)
    team = TeamMember.objects.all()
    return render(request, 'index.html', {
        "SubTitle":SubTitle,
        "WebsiteName":WebsiteName,
        "Features" : Features,
        "TeamMember1" : TeamMember1,
        "team" : team,
    })