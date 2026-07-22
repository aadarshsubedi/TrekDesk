from rest_framework import serializers
from .models import Booking
from datetime import date



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
    
    def validate_start_date(self,value):
        if value<date.today():
            raise serializers.ValidationError("Start date cannot be in the Past")
        return value
    
    def validate_no_of_people(self,value):
        if value<1:
            raise serializers.ValidationError("No.of people must be atleast 1")
        return value