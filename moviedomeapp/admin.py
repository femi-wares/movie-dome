from django.contrib import admin
from .models import movies,series,staff,related

# Register your models here.

admin.site.register(movies)
admin.site.register(series)
admin.site.register(staff)
admin.site.register(related)
