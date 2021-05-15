from django.urls import path

from employer.views import JobDetailView, JobCreateView

urlpatterns = [
    path('<slug:company>/<slug:slug>/', JobDetailView.as_view(), name='job_detail'),
    path('job/add/', JobCreateView.as_view(), name='job_add'),
]