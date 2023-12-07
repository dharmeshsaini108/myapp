from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.


# This is customization
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','department')
    list_editable=('working','emp_id')
    search_fields=('name',)
    list_filter=('working',)



admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
