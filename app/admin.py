from django.contrib import admin
from .models import bloodbankdata

class bloodbankAdmin(admin.ModelAdmin):
	list_display = ['id', 'Hospital_name', 'State', 'District', 'Contact', 'Address']
	ordering = ['id']
admin.site.register(bloodbankdata, bloodbankAdmin)
