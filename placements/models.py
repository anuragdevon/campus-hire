from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.CharField(max_length=20)


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
