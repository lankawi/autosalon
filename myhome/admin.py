from django.contrib import admin

from .models import Brand, Modell, Body_type, Body_color, Country, Insurance, Automobile, Type_of_service, Service

admin.site.register(Brand)
admin.site.register(Modell)
admin.site.register(Body_type)
admin.site.register(Body_color)
admin.site.register(Country)
admin.site.register(Insurance)
admin.site.register(Automobile)
admin.site.register(Type_of_service)
admin.site.register(Service)