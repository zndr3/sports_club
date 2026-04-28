from django import forms
from .models import Facility, Member, Booking

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'surname', 'recommendedby', 'address', 'zipcode', 'telephone', 'joindate']

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'membercost', 'guestcost', 'initialoutlay', 'monthlymaintenance']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['memid', 'facid', 'starttime', 'slots']
        widgets = {
            'memid': forms.Select(attrs={'class': 'form-control'}),
            'facid': forms.Select(attrs={'class': 'form-control'}),
            'starttime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'slots': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'memid': 'Member',
            'facid': 'Facility',
            'starttime': 'Start Time',
            'slots': 'Slots',
        }