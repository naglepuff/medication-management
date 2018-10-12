from django.urls import path 
from medications import views 

urlpatterns = [
    path('patients/', views.PatientList.as_view()),
    path('medications/', views.MedicationList.as_view()),
    path('assignments/', views.AssingmentList.as_view()),
    path('assignments/patient/<int:pid>/', views.assignment_by_patient),
    path('assignments/patient/<int:pid>/<int:mid>/', views.remove_medication_assignment),
]