from django.contrib import admin
from .models import Person

from import_export.admin import ImportExportModelAdmin

class PersonAdmin(ImportExportModelAdmin):
    pass
    # for slug to prepopulate in admin. 
    # @TODO look into this more
    # prepopulated_fields = {'slug': ('first_name', 'last_name',)}


admin.site.register(Person, PersonAdmin)
