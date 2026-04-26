from multiprocessing import context
from django.db.models import Count
from django.template import loader
from .models import Member, Facility, Booking
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberForm, FacilityForm

def member_list(request):
    members = Member.objects.all() # No need for .values() if using dots in templates
    return render(request, 'member_list.html', {'members': members})

def member_create(request):
    form = MemberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save() 
        return redirect('member_list')
    return render(request, 'member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member_form.html', {'form': form, 'edit_mode': True})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect('member_list')
    return render(request, 'member_confirm_delete.html', {'member': member})

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'facility_list.html', {'facilities': facilities})

def facility_create(request):
    form = FacilityForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save() 
        return redirect('facility_list')
    return render(request, 'facility_form.html', {'form': form})

def facility_update(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == "POST":
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'facility_form.html', {'form': form, 'edit_mode': True})

def facility_delete(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == "POST":
        facility.delete()
        return redirect('facility_list')
    return render(request, 'facility_confirm_delete.html', {'facility': facility})

def booking_list(request):
  bookings = Booking.objects.values('facid__name').annotate(count_facid=Count('facid')).order_by('facid__name')  
  return render(request, 'booking_list.html', {'bookings': bookings})

def main(request):
    # Context dictionary to pass data to the HTML
    context = {
        'title': 'Welcome to Sports Club Management',
    }
    return render(request, 'main.html', context)