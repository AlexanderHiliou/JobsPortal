from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView

from employer.company.models import Company
from django.utils.text import slugify
from django.db import IntegrityError

from employer.job.models import Job
from django.core.exceptions import ObjectDoesNotExist


class CompanyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'company/company_add.html'
    model = Company
    fields = ['name', 'field_of_activity', 'short_description', 'logo', 'location', 'created_at', 'amount_of_workers',
              'phone', 'website', 'email', 'facebook_url', 'google_plus_url', 'dribbble_url', 'pinterest_url',
              'twitter_url', 'github_url', 'instagram_url', 'youtube_url', 'company_detail']

    def form_valid(self, form):
        form.instance.employer = self.request.user.userprofile
        try:
            form.instance.slug = slugify(form.instance.name)
            return super().form_valid(form)
        except IntegrityError:
            latest_id = form.instance.__class__.objects.last().pk
            form.instance.slug = slugify(f'{form.instance.name}-{latest_id}')
            return super().form_valid(form)

    def test_func(self):
        """ Access is allowed only for Employers without any company """
        user_is_employer = self.request.user.userprofile.is_employer
        self.without_company = None
        if user_is_employer:
            try:
                self.request.user.userprofile.company
            except ObjectDoesNotExist:
                self.without_company = True
            else:
                self.without_company = False
        user = user_is_employer and self.without_company
        return user


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    slug_field = 'slug'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_jobs'] = Job.objects.filter(company=self.object).order_by('-created_at')[:5]
        return context
