from django.urls import path
from .views import BookingListCreateView,BookingDetailView,UpcomingBookingView
urlpatterns=[
    path("bookings",BookingListCreateView.as_view(),name="booking-list-create"),
    path("bookings/<int:booking_id>",BookingDetailView.as_view(),name="booking-detail"),
    path("bookings/upcoming",UpcomingBookingView.as_view(),name="booking-upcoming")
]