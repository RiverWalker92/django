from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from management.models import Layout, Content, SmallContent, TeamMember

#from django.http import Http404
from django.shortcuts import render



def index(request):
    Front_page_title = Layout.objects.get(title_id="front_page_title")
    About = Layout.objects.get(title_id="about")
    Video = Layout.objects.get(title_id="video")
    Contact = Layout.objects.get(title_id="contact")
    Features = Content.objects.get(title_id="features")
    Team = TeamMember.objects.all()
    return render(request, 'index.html', {
        "Front_page_title":Front_page_title,
        "Features" : Features,
        "About":About,
        "Video":Video,
        "Team" : Team,
        "Contact":Contact,
    })