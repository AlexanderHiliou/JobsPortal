from django.views.generic import DetailView, CreateView

from employer.models import Job


class JobDetailView(DetailView):
    model = Job
    slug_field = 'slug'
    template_name = 'employer/job_detail.html'
    context_object_name = 'job'

class JobCreateView(CreateView):
    template_name = 'employer/job_add.html'
    model = Job
    fields = ['title']
