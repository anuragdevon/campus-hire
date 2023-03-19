from django.urls import path
from .views import StudentList, StudentDetail, CompanyList, CompanyDetail, JobPostingList, JobPostingDetail, PlacementList, PlacementDetail

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetail.as_view()),
    path('jobpostings/', JobPostingList.as_view()),
    path('jobpostings/<int:pk>/', JobPostingDetail.as_view()),
    path('placements/', PlacementList.as_view()),
    path('placements/int:pk/', PlacementDetail.as_view()),
]