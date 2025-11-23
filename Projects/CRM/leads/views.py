from django.http import HttpResponse
from django.shortcuts import render
from .models import Agent, Lead
from .forms import LeadForm

# #Functional View
# def home_page(request):
#  return HttpResponse("Hello World!")

def lead_detail(request,pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    print(lead)
    return render(request, "leads/lead_details.html", context)
    

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"lead_list.html",context)

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                age = age
            )
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html",context)