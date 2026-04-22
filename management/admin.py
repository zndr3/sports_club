from django.contrib import admin
from .models import Member, Facility, Booking

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  
    def full_name(self, obj):
        return f"{obj.firstname} {obj.surname}"

    list_display = ('full_name', 'joindate', 'telephone')
    list_display_links = ('full_name',)

admin.site.register(Member, MemberAdmin)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'membercost', 'guestcost', 'initialoutlay', 'monthlymaintenance')
    list_display_links = ('name',)
    
admin.site.register(Facility, FacilityAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('facid', 'memid', 'starttime', 'slots')
    list_display_links = ('facid', 'memid')

admin.site.register(Booking, BookingAdmin)

