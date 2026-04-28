from django.db.models import Count
from django.template import loader
from .models import Member, Facility, Booking
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberForm, FacilityForm, BookingForm

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

# def booking_list(request):
#   bookings = Booking.objects.values('facid__name').annotate(count_facid=Count('facid')).order_by('facid__name')  
#   return render(request, 'booking_list.html', {'bookings': bookings})


def booking_by_facility(request, facid):
    bookings = (
        Booking.objects
        .filter(facid_id=facid)
        .select_related('facid', 'memid')
        .order_by('starttime')
    )

    return render(request, 'booking_by_facility.html', {
        'bookings': bookings,
        'facility_id': facid
    })

def booking_list(request):
    # Get all facilities with their booking counts using proper related objects
    facilities = Facility.objects.annotate(
        total=Count('booking')
    ).order_by('name')

    return render(request, 'booking_list.html', {'facilities': facilities})

def booking_create(request):
    form = BookingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('booking_list')

    return render(request, 'booking_form.html', {'form': form})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    form = BookingForm(request.POST or None, instance=booking)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('booking_by_facility', facid=booking.facid_id)

    return render(request, 'booking_form.html', {'form': form, 'edit_mode': True})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    facid = booking.facid_id

    if request.method == "POST":
        booking.delete()
        return redirect('booking_by_facility', facid=facid)

    return render(request, 'booking_confirm_delete.html', {'booking': booking})

def main(request):
    # Context dictionary to pass data to the HTML
    context = {
        'title': 'Welcome to Sports Club Management',
    }
    return render(request, 'main.html', context)