from django.views.generic import DetailView, CreateView

from employer.models import Job
from django.utils.text import slugify


class JobDetailView(DetailView):
    model = Job
    slug_field = 'slug'
    template_name = 'employer/job_detail.html'
    context_object_name = 'job'


class JobCreateView(CreateView):
    template_name = 'employer/job_add.html'
    model = Job
    fields = ['title', 'short_description', 'category', 'application_url', 'location', 'type_of_employment', 'salary',
              'working_hours', 'experience', 'academic_degree', 'job_detail']

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)

    def form_valid(self, form):
        form.instance.company = self.request.user.userprofile.company
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


