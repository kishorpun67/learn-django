###Python Django Commnad
```python
# installation  for danjo
pip install django

# create project command 
django-admin startproject projectname

# start project 
python manage.py runserver
 
# create app in django 
python manage.py startapp myapp

# create migrations files
python manage.py makemigrations

#create database of migration of files
python manage.py migrate

# for entering into shell 
python manage.py shell 


#Orm queries 
Student.objects.create() # store new data in database
Student.objects.filter(id=id) # where to fetch the specfice id
Student.objects.filter(id=id).exists() # check user is exists or not and return boolean value
Student.objects.all().order_by('field_name') # get date in ascending order
Student.objects.all().order_by('-field_name')[0:2] # get date in descingding order with limit
Student.objects.filter(field_name__gte = "value") # get data greater than value
Student.objects.filter(field_name__lte = "value") # get data less than value
Student.objects.filter(student_name__icontains = 'field_value')[0:1] # for seraching data with limitation
Student.objects.filter(filed_name__startswith = 'am') # get data starts with field name
Student.objects.filter(filed_name__enswith = 'a') # get data ends with field name
Student.objects.filter(department__department= "Civil")  # get data where relate to civil and __department refer id and department in department table  
Student.objects.filter(department__department__in = array) #fetch data with comparing with array
Student.objects.exclude(department__department__in = ['Civil']) ## get data expect civil include
Student.objects.all().values()  # it graps all value in to dict selerize we cannot relation ship get value
Student.objects.values_list('id', 'student_name'), # fetch the values which filed pass in list and it always return tupl

# Aggregation is performing action in a single column like,su averagem,avarage
#  Annotion is perform action in multiple column like,group

# import first 
from django.db.models import *
# single aggregate
Student.objects.aggregate(Avg('student_age')) # calculate avarage of student_age
Student.objects.aggregate(Max('student_age')) #  max of student_age
Student.objects.aggregate(Min('student_age')) #  min of student_age
Student.objects.aggregate(Sum('student_age')) #  sum of student_age

#annotate
Student.objects.values('student_age').annotate(Count('student_age')) #  show age and count same age
Student.objects.values('student_age', 'department').annotate(Count('student_age'), Count('department'))





```