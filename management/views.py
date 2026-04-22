from django.http import HttpResponse
from django.template import loader
from .models import Member, Facility, Booking

def facilities(request):
  facilities = Facility.objects.all().values()
  template = loader.get_template('facilities.html')
  context = {
    'facilities': facilities,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())