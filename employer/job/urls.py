from django.urls import path

from employer.job.views import JobDetailView, JobUpdateView, JobDeleteView, JobCreateView, JobManage

urlpatterns = [
    path('<slug:company_slug>/<slug:slug>/', JobDetailView.as_view(), name='job_detail'),
    path('<slug:company>/<slug:slug>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<slug:company>/<slug:slug>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('add/', JobCreateView.as_view(), name='job_add'),
    path('manage/', JobManage.as_view(), name='job_manage'),

]
