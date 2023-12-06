from faker import Faker
import random
from .models import *
fake = Faker()

def create_subject_marks(n: int) -> None:
    try:
        student_objs = Student.objects.all()
        subjects = Subject.objects.all()

        for student in student_objs:
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0, 100)
                )
    except:
        print(f'An error occurred')
def seed_db(n=10)->None:
    department_objs = list(Department.objects.all())
    if not department_objs:
        print("No departments available.")
        return

    for _ in range(n):
        random_index = random.randint(0, len(department_objs) - 1)
        student_id = f'STU-0{random.randint(100, 999)}'
        department = department_objs[random_index]
        student_name = fake.name()
        student_email = fake.email()
        student_age= random.randint(20,30)
        student_address = fake.address()
        student_id_obj = StudentID.objects.create(student_id = student_id)
        Student.objects.create(
            department = department,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address
        )

def generate_report_card():
        ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks')    
        current_rank = -1;
        i = 1;
        for mark in ranks:
            ReportCard.objects.create(
                student = mark,
                student_rank = i 
            )
            i = i+1
           