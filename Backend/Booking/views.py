from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .models import Booking
from .serializers import BookingSerializers
from datetime import date

class BookingListCreateView(ListCreateAPIView):
    queryset=Booking.objects.all().order_by("start_date")
    serializer_class=BookingSerializers
    
class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializers
    lookup_url_kwarg="booking_id"
    
class UpcomingBookingView(ListAPIView):
    serializer_class=BookingSerializers
    
    def get_queryset(self):
        return Booking.objects.filter(start_date__gte=date.today()).order_by("start_date")