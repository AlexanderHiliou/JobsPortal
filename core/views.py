from django.views.generic import ListView
from allauth.account.views import SignupView

from employer.models import Job
from .models import Userprofile


class IndexView(ListView):
    model = Job
    queryset = Job.objects.all().select_related('company').only('title', 'location', 'company', 'type_of_employment')
    template_name = 'core/index.html'
    context_object_name = 'jobs'


class UserSignupView(SignupView):
    template_name = 'account/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        account_type = self.request.POST.get('account_type')
        if account_type == 'employer':
            Userprofile.objects.create(user=user, is_employer=True)
        else:
            Userprofile.objects.create(user=user)
        return response
