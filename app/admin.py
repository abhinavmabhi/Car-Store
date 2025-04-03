from django.contrib import admin
from django.utils.html import mark_safe
from .models import Brand, Car_Type, CarModel, Car, Fuel_Type, Transmission_Type


# Custom Admin for Car Model
class CarAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name', 'get_car_name', 'get_car_type', 'fuel_type', 'price', 'year', 'total_km_run')
    list_display_links = ('image_tag', 'get_car_name')
    search_fields = ('brand__name', 'model__name', 'type__name')  
    list_filter = ('fuel_type', 'transmission', 'year', 'type')

    # Display the car image in the list view
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"

    image_tag.short_description = 'Car Image'

    # Display the car name (Brand + Model)
    def get_car_name(self, obj):
        return f"{obj.brand.name} {obj.model.name}"

    get_car_name.short_description = 'Car Name'

    # Display the car type (type name)
    def get_car_type(self, obj):
        return obj.type.name

    get_car_type.short_description = 'Car Type'

    # Organize fields in the admin form
    fieldsets = (
        (None, {
            'fields': ('brand',"name",'type', 'model', 'fuel_type', 'transmission', 'price', 'mileage', 'color', 'owner_count', 'description', 'image', 'is_available', 'year', 'total_km_run')
        }),
    )

    # Ordering the list of cars (newest first based on created date)
    ordering = ('-created_date',)  # Optional: Order by created date

    # You can also add custom methods for other fields if necessary
    # Ordering the ForeignKey field "brand" in ascending order
    ordering = ('brand',)

    # Customizing the brand field to display brands in ascending order
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['brand'].queryset = Brand.objects.all().order_by('name')
        return form

# Register your models with the custom admin
admin.site.register(Brand)
admin.site.register(Car_Type)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
