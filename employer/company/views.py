from django.views.generic import CreateView, DetailView

from employer.company.models import Company
from django.utils.text import slugify

from employer.job.models import Job


class CompanyCreateView(CreateView):
    template_name = 'company/company_add.html'
    model = Company
    fields = ['name', 'field_of_activity', 'short_description', 'logo', 'location', 'created_at', 'amount_of_workers',
              'phone', 'website', 'email', 'facebook_url', 'google_plus_url', 'dribbble_url', 'pinterest_url',
              'twitter_url', 'github_url', 'instagram_url', 'youtube_url', 'company_detail']

    def form_valid(self, form):
        form.instance.employer = self.request.user.userprofile
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)

    # def test_func(self):
    #     user = self.request.user.userprofile.is_employer and self.request.user.userprofile.company
    #     return user


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    slug_field = 'slug'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_jobs'] = Job.objects.filter(company=self.object)[:5]
        return context
