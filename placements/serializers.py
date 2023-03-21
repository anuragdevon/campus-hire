from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from .models import Student, Company, JobPosting, Placement


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )

    class Meta:
        model = Student
        # exclude = ["password"]
        fields = "__all__"


class JobPostingSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data["salary_min"] <= 0 or data["salary_max"] <= 0:
            raise serializers.ValidationError("Salary range must be greater than 0.")
        return data

    class Meta:
        model = JobPosting
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    job_postings = JobPostingSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = "__all__"


# Check delete options

# Student, Job posting cannot be post, companies can be post
# Similiar to companies, remove placements, and add it directly in get
# Try to update directly on detail view similiar to companies
