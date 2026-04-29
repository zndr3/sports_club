from rest_framework.viewsets import ModelViewSet
from .models import Booking, Facility, Member
from .serializers import (
    BookingSerializer,
    FacilitySerializer,
    MemberSerializer
)

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class FacilityViewSet(ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer