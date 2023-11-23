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
Student.objects.all().order_by('field_name') # get date in ascending order
Student.objects.all().order_by('-field_name')[0:2] # get date in descingding order with limit
Student.objects.filter('field_name__gte' = "value") # get data greater than value
Student.objects.filter('field_name__lte' = "value") # get data less than value
Student.objects.filter('student_name__icontains' = 'field_value')[0:1] # for seraching data with limitation




```