Medication Management:

I have chosen to write the exercise using Django and Django-REST framework,
due to the simplicity and clean coding. Django is also the web framework
that I have the most experience with. 

To run the application locally, you need to activate the virtual environment,
which is in the same folder as this document. Run

source env/bin/activate  

to activate the virtual environment. The requrements should be installed there.
If not, install them with pip:

pip install -r requirements.txt

After that, cd into the medication_management folder. This is where all of 
the source code is. The Django app with add the source code is called 
medications. The important files are models.py, serializers.py, views.py, 
and urls.py. 

To run the app:

python manage.py runserver 

This should activate the application. I tested it using httpie. 

The urls that are used to complete the 4 tasks specified are as follows:

http://127.0.0.1:8000/patients/

This url retireves all patients if the request method is GET. If the method
is POST and there is JSON data sent along with it (a patient needs a name)
it creates a new patient. 

http://127.0.0.1:8000/medications/ 

Retrieves the list of all medications if the method is GET. If it is POST, and
there is a value for a name field sent along then a new medicaton with the 
given name is added to the database. 

http://127.0.0.1:8000/assignments/

Retrieves a list of all medication assigments with GET. If the method is POST,
data for 'patient' and 'medication' need to be sent as well. This time as 
integers, as they are foreign key references (one for patient, one for 
medication). 

http://127.0.0.1:8000/assignments/patients/<int:pid>/<int:mid>/ 

Send a request with DELETE as the method to this url and it deletes the 
medication assignment where patient's id is pid and medication's id is mid
