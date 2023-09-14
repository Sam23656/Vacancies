from django.contrib import admin


# Register your models here.
from app.models import *

admin.site.register(Company)
admin.site.register(VacancyTitle)
admin.site.register(Requirement)
admin.site.register(Job)
