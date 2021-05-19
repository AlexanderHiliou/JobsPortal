from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.db import IntegrityError

from django.utils.text import slugify

from employer.job.models import Job


class JobDetailView(DetailView):
    model = Job
    slug_field = 'slug'
    template_name = 'job/job_detail.html'
    context_object_name = 'job'


class JobManage(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job/job_manage.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        queryset = Job.objects.filter(company=self.request.user.userprofile.company).select_related('company')
        return queryset


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'job/job_add.html'
    model = Job
    fields = ['title', 'short_description', 'category', 'application_url', 'location', 'type_of_employment', 'salary',
              'working_hours', 'experience', 'academic_degree', 'job_detail']

    def form_valid(self, form):
        form.instance.company = self.request.user.userprofile.company
        try:
            form.instance.slug = slugify(form.instance.title)
            return super().form_valid(form)
        except IntegrityError:
            latest_id = form.instance.__class__.objects.last().pk
            form.instance.slug = slugify(f'{form.instance.title}-{latest_id}')
            return super().form_valid(form)

    def test_func(self):
        user = self.request.user.userprofile.is_employer and self.request.user.userprofile.company
        return user


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'job/job_update.html'
    model = Job
    slug_field = 'slug'
    fields = ['title', 'short_description', 'category', 'application_url', 'location', 'type_of_employment', 'salary',
              'working_hours', 'experience', 'academic_degree', 'job_detail']

    def test_func(self):
        obj = self.get_object()
        user = self.request.user == obj.company.employer.user
        return user


class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('index_view')
    template_name = 'job/job_delete_confirmation.html'
