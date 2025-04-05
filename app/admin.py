from django.contrib import admin
from django.utils.html import mark_safe
from .models import Brand, Car_Type, CarModel, Car, Fuel_Type, Transmission_Type
from django.contrib.auth.models import Group



# ----------------------------
# Custom Admin for Car Model
# ----------------------------
class CarAdmin(admin.ModelAdmin):

    # Fields displayed in list view
    list_display = (
        'image_tag', 'name', 'get_car_name', 'get_car_type', 'price', 'year', 'total_km_run', 'delete_button'
    )
    list_display_links = ('image_tag', 'get_car_name')
    search_fields = ('brand__name', 'model__name', 'type__name')
    list_filter = ('fuel_type', 'transmission', 'year', 'type', 'is_available')
    ordering = ('brand',)  # Optional: Order by brand name

    # ------------------------
    # Display car image
    # ------------------------
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"
    image_tag.short_description = 'Car Image'

    # ------------------------
    # Car Name (Brand + Model)
    # ------------------------
    def get_car_name(self, obj):
        return f"{obj.brand.name} {obj.model.name}"
    get_car_name.short_description = 'Car Name'

    # ------------------------
    # Car Type
    # ------------------------
    def get_car_type(self, obj):
        return obj.type.name
    get_car_type.short_description = 'Car Type'

    # ------------------------
    # Delete Button in List
    # ------------------------
    def delete_button(self, obj):
        return mark_safe(f'<a href="/admin/app/car/{obj.pk}/delete/" class="button" style="color:white; background:red">Delete</a>')
    delete_button.short_description = 'Delete'

    # ------------------------
    # Form Field Ordering
    # ------------------------
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['brand'].queryset = Brand.objects.all().order_by('name')
        return form

    # ------------------------
    # Admin Form Layout
    # ------------------------
    fieldsets = (
        (None, {
            'fields': (
                'brand', 'name', 'type', 'model', 'fuel_type', 'transmission',
                'price', 'mileage', 'color', 'owner_count', 'description',
                'image','image1','image2','image3', 'is_available', 'year', 'total_km_run'
            )
        }),
    )


# ----------------------------
# Registering Models
# ----------------------------
admin.site.register(Brand)
admin.site.register(Car_Type)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.unregister(Group)