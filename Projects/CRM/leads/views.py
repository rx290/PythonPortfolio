from django.http import HttpResponse
from django.shortcuts import render
from .models import Lead

#Functional View
def home_page(request):
 return HttpResponse("Hello World!")

def lead_detail(request,pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("Here is the detail view!")
    

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"leads/lead_list.html",context)