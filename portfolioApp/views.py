from django.shortcuts import render
from portfolioApp.models import Navbar, Profile, Skill, Services, Number_Area, Project, Testimonial, Personal_Information, Client_Name
# Create your views here.
def index(request):
    context = {}
    context['nav_list'] = Navbar.objects.all()
    context['profile'] = Profile.objects.all().first()
    context['skill'] = Skill.objects.all()
    context['services'] = Services.objects.all()
    context['number_area'] = Number_Area.objects.all()
    context['project'] = Project.objects.all()
    context['testimonial'] = Testimonial.objects.all()
    context['info'] = Personal_Information.objects.all()
    context['brand'] = Client_Name.objects.all()


    return render(request, "index.html", context)
