from django.urls import path

from employer.company.views import CompanyCreateView

urlpatterns = [
    path('new-company', CompanyCreateView.as_view(), name='new_company'),
]