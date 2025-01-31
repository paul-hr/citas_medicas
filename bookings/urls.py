from django.urls import path

from .views import ListAppointmentView, DetailAppointmentView,ListMedicalNoteView,DetailMedicalNoteView

urlpatterns = [
    path('appoinments/', ListAppointmentView.as_view()),
    path('appoinments/<int:pk>/', DetailAppointmentView.as_view()),
    path('medical/', ListMedicalNoteView.as_view()),
    path('medical/<int:pk>/', DetailMedicalNoteView.as_view()),
]