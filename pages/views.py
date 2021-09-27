from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing 
from owners.models import Owner 

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices

    }

    return render(request,'pages/index.html', context)

def about(request):
    #get all realtor
    owners = Owner.objects.order_by('-hire_date')

    #get mvp 
    mvp_owners = Owner.objects.all().filter(is_mvp=True)

    context = {
        'owners': owners,
        'mvp_owners': mvp_owners
    }
    return render(request,'pages/about.html', context)

