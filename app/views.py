from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from .models import Car,Car_Type,Fuel_Type
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
from .forms import Contact_Form

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

    year_filter = request.GET.get("year", "")   

    year_ranges = [
    ("2001-2005", "2001 - 2005"),
    ("2006-2010", "2006 - 2010"),
    ("2011-2015", "2011 - 2015"),
    ("2016-2020", "2016 - 2020"),
    ("2021-2025", "2021 - 2025"),
]

    if year_filter:
        try:
            start_year, end_year = map(int, year_filter.split("-"))
            qs = qs.filter(year__gte=start_year, year__lte=end_year)
        except:
            pass

    context = {
    "car": qs,
    "search": search,
    "car_types": car_types,
    "selected_year": year_filter,
    "selected_car_type": car_type,
    "selected_transmission": transmission,
    "selected_fuel_type": fuel_type,
    "selected_owner_count": owner_count,
    "year_ranges": year_ranges, 

}
    return render(request, "CarList.html", context)



def Car_details_view(request,id):

    car=get_object_or_404(Car,id=id)

    return render(request,"car_details.html",{"car":car})



def about_view(request):
    
    return render(request,"about.html")

def Service_view(request):

    return render(request,"service.html")



def Contact_view(request):
    if request.method=="POST":
        form=Contact_Form(request.POST)
        if form.is_valid():
            messages.success(request,"Successfully submitted the Form")
            contact=form.save()

            subject=f"New Enquiry Submitted - {contact.message}"

            message=f"""

Name: {contact.name}
Phone: {contact.phone}
email: {contact.email}
Message: {contact.message}            
"""
            
            html_message = f"""
            <p><strong>Name:</strong> {contact.name}</p>
            <p><strong>Phone:</strong> <a href="tel:{contact.phone}">{contact.phone}</a></p>
            <p><strong>Email:</strong> {contact.email}</p>
            <p><strong>Message:</strong> {contact.message}</p>
            """
            send_mail(
                subject=subject,
                message=message,
                from_email="abhinavabhi192018@gmail.com",
                recipient_list=["abhinavvvv.m@gmail.com"],
                fail_silently=False,
                html_message=html_message,
            )
        else:
            messages.error(request,"Form submission failed. Please try again")

    else:
        form=Contact_Form()
    return render(request,"contact.html",{"form":form,})

def Gallery_view(request):
    return render(request,'gallery.html')