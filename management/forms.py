from django import forms
from .models import Facility, Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'surname', 'recommendedby', 'address', 'zipcode', 'telephone', 'joindate']

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'membercost', 'guestcost', 'initialoutlay', 'monthlymaintenance']