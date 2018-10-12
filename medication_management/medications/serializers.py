from rest_framework import serializers 
from medications.models import Patient, Medication, Assignment 

"""
Django-rest seriazlizers are responsible for turning django models into JSON and vice-versa
Here I'm just using the default set up for serializers. Each one is associated with a model,
and the fields to be serialized are also specified.
"""

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment 
        fields = ('patient', 'medication',) # note that these are FK ids. one improvement could be to have them render as strings

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient 
        fields = ('id', 'name',)  

class  MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication 
        fields = ('id', 'name',) 

