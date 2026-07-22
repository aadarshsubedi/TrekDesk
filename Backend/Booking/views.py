from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from .models import Booking
from .serializers import BookingSerializers

class BookingListCreateView(ListCreateAPIView):
    queryset=Booking.objects.all().order_by("start_date")
    serializer_class=BookingSerializers
    
class BookingDetailView(RetrieveAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializers
    lookup_url_kwarg="booking_id"
    