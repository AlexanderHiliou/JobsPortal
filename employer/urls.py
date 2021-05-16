from django.urls import path

from employer.views import JobDetailView, JobCreateView, JobUpdateView

urlpatterns = [
    path('<slug:company>/<slug:slug>/', JobDetailView.as_view(), name='job_detail'),
    path('<slug:company>/<slug:slug>/update/', JobUpdateView.as_view(), name='job_update'),
    path('job-add/', JobCreateView.as_view(), name='job_add'),
]