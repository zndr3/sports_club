from multiprocessing import context
from django.db.models import Count
from django.http import HttpResponse
from django.template import loader
from .models import Member, Facility, Booking

def facility_list(request):
  facilities = Facility.objects.all().values()
  template = loader.get_template('facility_list.html')
  context = {
    'facilities': facilities,
  }
  return HttpResponse(template.render(context, request))

def booking_list(request):

  bookings = Booking.objects.values('facid__name').annotate(count_facid=Count('facid')).order_by('facid__name')
  template = loader.get_template('booking_list.html')
  context = {
    'bookings': bookings,
  }
  return HttpResponse(template.render(context, request))

def member_list(request):
  members = Member.objects.all().values()
  template = loader.get_template('member_list.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())