from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import Car,Car_Type,Fuel_Type
from django.db.models import Q

# Create your views here.

def Home_page_view(request):
    search = request.GET.get("q", "")

    if search:
        return redirect(f"/car/list/?q={search}") 

    return render(request, "Home.html")

def List_all_cars(request):
    search=request.GET.get("q","")
    min_price = request.GET.get("min_price", None)
    max_price = request.GET.get("max_price", None)
    min_km = request.GET.get("min_km",None)
    max_km = request.GET.get("max_km",None)
    car_type = request.GET.get("car_type", "")
    transmission = request.GET.get("transmission", "")
    fuel_type = request.GET.get("fuel_type", "")
    owner_count=request.GET.get("owner_count","")


    qs=Car.objects.all()
    car_types = Car_Type.objects.all()

    if search:
        qs=qs.filter(
            Q(brand__name__icontains=search)|
            Q(name__icontains=search)|
            Q(type__name__icontains=search)|
            Q(model__name__icontains=search)|
            Q(fuel_type__icontains=search)|
            Q(transmission__icontains=search)
        )
        


    if min_price and max_price:
        qs=qs.filter(price__gte=min_price,price__lte=max_price)
    if min_km and max_km:
        qs=qs.filter(total_km_run__gte=min_km,total_km_run__lte=max_km)
    if car_type:
        qs=qs.filter(type__name=car_type)
    if transmission:
        qs=qs.filter(transmission=transmission)
    if fuel_type:
        qs=qs.filter(fuel_type=fuel_type)
    if owner_count:
        qs=qs.filter(owner_count=owner_count)

    return render(request,"CarList.html",{"car":qs,"search":search,"car_types": car_types})

def Car_details_view(request,id):

    car=get_object_or_404(Car,id=id)

    return render(request,"car_details.html",{"car":car})





