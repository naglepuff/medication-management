from medications.models import Patient, Medication, Assignment 
from medications.serializers import PatientSerializer, MedicationSerializer, AssignmentSerializer 

from django.http import HttpResponse

from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import generics

"""
Here is the meat of the API. I've provided "views" for the requirements specified for the task,
as well as a few others, to be a tad more thorough. 

To see url path specifications, see medications/urls.py

This API doesn't yet have any update functionality,
and it doesn't have an retrieve/update/delete for a specific instance of Patient or Medication. It also 
lacks the ability to retirieve a single assignment. All of this is functionality that could be implemented 
relatively easily in the future for a more complete application. 

Another change that could be made it adding user authentication.
"""

class PatientList(generics.ListCreateAPIView):
    """
    class that provides functionality to retrieve all Patients and POST a new one using
    rest_frameworks built-in generics library.
    """
    queryset = Patient.objects.all() 
    serializer_class = PatientSerializer

class MedicationList(generics.ListCreateAPIView):
    """See PatientList"""
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class AssingmentList(generics.ListCreateAPIView):
    """See PatientList"""
    queryset = Assignment.objects.all() 
    serializer_class = AssignmentSerializer

@api_view(['GET',])
def assignment_by_patient(request, pid):
    """
    A way to get all medication assignments for a given user.
    inputs: request (an http request), pid (a patient id)
    output: a reponse object
    """
    try:
        ### Using django's ORM to get the patient specified, and then using that information to get their assignments
        patient = Patient.objects.get(pk=pid) 
        patient_assignments = Assignment.objects.filter(patient=patient) 
    except Patient.DoesNotExist:
        # if the patient does not exist we respond with 404
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 

    # if the patient does indeed exist we use the serizlizer jsonify the assignments and return them in the response
    if request.method == 'GET':
        serializer = AssignmentSerializer(patient_assignments, many=True) 
        return Response(serializer.data)

@api_view(['DELETE',])
def remove_medication_assignment(request, pid, mid):
    """
    Deletes a given assignment corresponding a patient and medication
    inputs: request (http request), pid (the patient id), mid (the medication id) 
    outputs: an http response
    """
    try:
        # Again, make sure the patient, medication, and assignment exist before doing anything with them
        # and if not, return 404
        patient = Patient.objects.get(pk=pid) 
        medication = Medication.objects.get(pk=mid)
        assignment = Assignment.objects.filter(patient=patient).filter(medication=medication)[0]
    except (Patient.DoesNotExist, Assignment.DoesNotExist, Medication.DoesNotExist) as e:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Given that the assingment exists, delete it from the database.
    assignment.delete() 
    return Response(status=status.HTTP_204_NO_CONTENT) 