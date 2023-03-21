from django.http import HttpResponse
from rest_framework import generics
from datetime import datetime
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Company, JobPosting, Placement
from .serializers import (
    StudentSerializer,
    CompanySerializer,
    JobPostingSerializer,
    PlacementSerializer,
)


def home_ping(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# -------------------------------------GET----------------------------------
class StudentPagination(PageNumberPagination):
    page_size = 10


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination


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


class StudentPlacementList(generics.ListAPIView):
    serializer_class = PlacementSerializer

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        return Placement.objects.filter(student_id=student_id)


class JobPostingList(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "qualifications"]


# -------------------------------------GET----------------------------------

# --------------------------------------POST---------------------------------
class PlacementCreate(generics.CreateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer

    def create(self, request, *args, **kwargs):
        student_data = request.data.pop("student")
        job_posting_data = request.data.pop("job_posting")
        student_serializer = StudentSerializer(data=student_data)
        job_posting_serializer = JobPostingSerializer(data=job_posting_data)
        if student_serializer.is_valid() and job_posting_serializer.is_valid():
            student = student_serializer.save()
            job_posting = job_posting_serializer.save(
                company_id=job_posting_data["company"]
            )
            request.data["student"] = student.id
            request.data["job_posting"] = job_posting.id
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                {
                    "student": student_serializer.errors,
                    "job_posting": job_posting_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

class PlacementUpdate(generics.UpdateAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        student_data = request.data.pop('student')
        job_posting_data = request.data.pop('job_posting')
        student_serializer = StudentSerializer(instance.student, data=student_data)
        job_posting_serializer = JobPostingSerializer(instance.job_posting, data=job_posting_data)
        if student_serializer.is_valid() and job_posting_serializer.is_valid():
            student = student_serializer.save()
            job_posting = job_posting_serializer.save(company_id=job_posting_data['company'])
            request.data['student'] = student.id
            request.data['job_posting'] = job_posting.id
            return super().update(request, *args, **kwargs)
        else:
            return Response({
                'student': student_serializer.errors,
                'job_posting': job_posting_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class PlacementDetail(generics.RetrieveAPIView):
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        student_serializer = StudentSerializer(instance.student)
        job_posting_serializer = JobPostingSerializer(instance.job_posting)
        data = serializer.data
        data['student'] = student_serializer.data
        data['job_posting'] = job_posting_serializer.data
        return Response(data)


# --------------------------------------POST---------------------------------
