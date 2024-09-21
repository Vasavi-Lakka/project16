from django.contrib import admin # type: ignore

# Register your models here.
from app.models import *

admin.site.register(Dept)
admin.site.register(Emp)