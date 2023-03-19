from django.http import HttpResponse
from rest_framework import generics
from datetime import datetime

from .models import Student, Company, JobPosting, Placement
from .serializers import StudentSerializer, CompanySerializer, JobPostingSerializer, PlacementSerializer


def home_ping(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobPostingList(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobPostingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class PlacementList(generics.ListCreateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer

class PlacementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
