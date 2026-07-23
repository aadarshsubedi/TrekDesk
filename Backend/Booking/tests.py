from datetime import date, timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Booking

class BookingAPITests(APITestCase):
    def test_create_booking_success(self):
        """A booking with valid data should be created and return 201"""
        url=reverse("booking-list-create")
        future_date=(date.today()+timedelta(days=10) ).isoformat()
        
        data={
            "client_name":"Test Client",
            "trek_route":"Test Route",
            "start_date":future_date,
            "no_of_people":2,
            "deposite":True,
        }
        response= self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(),1)
    
    def test_create_booking_with_past_date_rejected(self):
        """ A Booking with the start_date in the past should be rejected with 404 response"""
        url=reverse("booking-list-create")
        past_date=(date.today()-timedelta(days=5)).isoformat()
        
        data={
            "client_name":"Late Booker",
            "trek_route":"Everest Base Camp",
            "start_date":past_date,
            "no_of_people":3,
            "deposite":False,
        }
        response= self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Booking.objects.count(),0)
    
    def test_create_booking_with_zero_people_rejected(self):
        """A Booking with the 0 people should be rejected with 404 response"""
        url=reverse("booking-list-create")
        future_date=(date.today()+ timedelta(days=10)).isoformat()
        data={
            "client_name":"Nobody",
            "trek_route":"Langtang",
            "start_date":future_date,
            "no_of_people":0,
            "deposite": False,
        }
        response=self.client.post(url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Booking.objects.count(),0)
        
    def test_gets_nonexistent_booking_returns_404(self):
        """Extracting the booking id which doesnot exist should return 404 response, not server crash """
        url=reverse("booking-detail",kwargs={"booking_id":999})
        response=self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
    def test_delete_booking_removes_it(self):
        """Deleting a booking should return 204 and actually remove it from the database"""
        booking=Booking.objects.create(
            client_name="To Be Deleted",
            trek_route="Pon Hill",
            start_date=date.today() + timedelta(days=5),
            no_of_people=2,
            deposite=True,
        )
        url=reverse("booking-detail",kwargs={"booking_id":booking.id})
        response=self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(),0)