from django.shortcuts import render
from django.template import loader 
from .models import Profile
import pdfkit 
from django.http import HttpResponse

# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        skills = request.POST.get('skills','')

        profile = Profile(name=name,
                        email=email,
                        phone=phone,
                        summary=summary,
                        degree=degree,
                        school=school,
                        university=university,
                        previous_work=previous_work,
                        skills=skills)
        profile.save()

    return render(request, 'pdf/accept.html')

def resume(request, id):
    profile = Profile.objects.get(pk=id)
    return render(request, "pdf/resume.html", {"profile":profile})


def resume_list(request):
    profiles_list = Profile.objects.all()
    return render(request, "pdf/resume_list.html", {"profiles_list":profiles_list})