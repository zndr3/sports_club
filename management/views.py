from multiprocessing import context
from django.db.models import Count
from django.template import loader
from .models import Member, Facility, Booking
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MemberForm

def member_list(request):
    members = Member.objects.all() # No need for .values() if using dots in templates
    return render(request, 'member_list.html', {'members': members})

from django.db.models import Max

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            # commit=False creates the object but doesn't send it to Supabase yet
            new_member = form.save(commit=False)

            # 1. Find the current highest memid in your table
            # If the table is empty, start at 0
            highest_id = Member.objects.aggregate(Max('memid'))['memid__max'] or 0

            # 2. Manually set the ID to the next available number
            new_member.memid = highest_id + 1
            # 3. Now send it to Supabase
            new_member.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})


def member_update(request, pk):
    # 'pk' stands for Primary Key (the memid)
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
    facilities = Facility.objects.all() # No need for .values() if using dots in templates
    return render(request, 'facility_list.html', {'facilities': facilities})

def booking_list(request):
  bookings = Booking.objects.values('facid__name').annotate(count_facid=Count('facid')).order_by('facid__name')  
  return render(request, 'booking_list.html', {'bookings': bookings})

def main(request):
    # Context dictionary to pass data to the HTML
    context = {
        'title': 'Welcome to Sports Club Management',
    }
    return render(request, 'main.html', context)