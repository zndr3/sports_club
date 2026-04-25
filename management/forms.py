from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'surname', 'recommendedby', 'address', 'zipcode', 'telephone', 'joindate'] # List the fields you want users to fill