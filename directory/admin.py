from django.contrib import admin
from .models import Person

from import_export.admin import ImportExportModelAdmin

class PersonAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
