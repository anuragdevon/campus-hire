from django.db import models
from django.db.models.signals import pre_save, post_save

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    @classmethod
    def get_placed_students(cls):
        return cls.objects.filter(status='Placed')
    
    @classmethod
    def get_available_students(cls):
        return cls.objects.filter(status='Available')

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    email = models.EmailField()


class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    qualifications = models.TextField()


class Placement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    date = models.DateField()
    is_accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student} - {self.job_posting} ({self.start_date} to {self.end_date})"

