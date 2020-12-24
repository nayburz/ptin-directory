from django.contrib import admin
from .models import Person # State

from import_export.admin import ImportExportModelAdmin

class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'state')
    


    # for slug to prepopulate in admin. 
    # @TODO look into this more
    # prepopulated_fields = {'slug': ('first_name', 'last_name',)}

# admin.site.register(State)
admin.site.register(Person, PersonAdmin)
