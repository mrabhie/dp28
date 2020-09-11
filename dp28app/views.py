from django.shortcuts import render,redirect
from django.http import HttpResponse
from dp28app.models import *

#whats new:here we are displaying the databse data to the user by using front end and views.
def createtopic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h2>topic added successfully</h2>")
        else:
            return HttpResponse("<h2>Topic is already exist in the table</h2>")
    return render(request,"createtopic.html")

def createwebpage(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        name=request.POST.get("name")
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=WebPage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h1>Webpage added successfully</h1>")
    topics=Topic.objects.all()
    return render(request,"createwebpage.html",context={'topics':topics})

def createaccess(request):
    if request.method=="POST":
        webpage=request.POST.get("webpage")
        datetime=request.POST.get("datetime")
        w=WebPage.objects.get_or_create(name=webpage)[0]
        d=AccessDetails.objects.get_or_create(webpage=w,datetime=datetime)[0]
        d.save()
        return HttpResponse("<h1>Datetime added successfully</h1>")
    webpages=WebPage.objects.all()
    return render(request,"createaccess.html",context={'webpages':webpages})

def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"displaytopic.html",\
        context={'topics':topics})

def display_webpages(request):
    webpages=WebPage.objects.all()
    return render(request,"displaywebpage.html",\
        context={'webpages':webpages})

def display_accessdetails(request):
    accessdetails=AccessDetails.objects.all()
    return render(request,"displayaccess.html",\
        context={'accessdetails':accessdetails})
#accessing the specific data present in the database by passing the pk
#in the url

def displaytopic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"displaytopic.html",context={'topics':topics})

def displaywebpage(request,webid):
    webpages=WebPage.objects.filter(id=webid)
    return render(request,"displaywebpage.html",context={'webpages':webpages})

def displayaccess(request,aid):
    accessdetails=AccessDetails.objects.filter(id=aid)
    return render(request,"displayaccess.html",context={'accessdetails':accessdetails})



