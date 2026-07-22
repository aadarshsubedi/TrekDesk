from rest_framework import serializers
from .models import Booking
class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=[
            "id",
            "client_name",
            "trek_route",
            "start_date",
            "no_of_people",
            "deposite",
            "created_at",
        ]
        read_only_fields=["id","created_at"]