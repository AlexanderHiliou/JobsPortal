from django.urls import path

from employer.company.views import CompanyCreateView, CompanyDetailView

urlpatterns = [
    path('<slug:slug>/detail/', CompanyDetailView.as_view(), name='company_detail'),
    path('new-company/', CompanyCreateView.as_view(), name='new_company'),
]