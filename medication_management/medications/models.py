from django.db import models


class Patient(models.Model):
    """
    A simple patient model. Django supplies an integer pk as a default. 
    I've also included a patient name field. 
    """
    name = models.CharField(max_length=100) 

class Medication(models.Model): 
    """
    A simple medication model. Includes a name field and default pk field.
    """
    name = models.CharField(max_length=100)  

class Assignment(models.Model): 
    """
    Here's a model called assignment. 
    An instance of an assignment assigns a medication to a patient.
    Each row of the associated relation contains foreign keys to a patient and a client. 
    Assignments are deleted when either the medication or the patient is.

    One potential update is the make the pair of FKs unique
    """
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) 

    # I want to order the assignments by patient in the DB
    class Meta:
        ordering = ('patient',) 