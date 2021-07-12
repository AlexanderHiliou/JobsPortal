from django.urls import path

from jobseeker.resume.views import ResumeCreateView

urlpatterns = [
    path('add/', ResumeCreateView.as_view(template_name="resume/resume-add.html"), name="resume_add"),
]
