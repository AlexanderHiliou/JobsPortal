from django.views.generic import ListView
from allauth.account.views import SignupView
from django.urls import reverse
from django.conf import settings

from employer.job.models import Job
from .models import Userprofile


class IndexView(ListView):
    """View of the main page"""
    model = Job
    queryset = Job.objects.order_by('-created_at').select_related('company').only('title', 'location', 'company',
                                                                                  'type_of_employment')[:5]
    template_name = 'core/index.html'
    context_object_name = 'jobs'


class UserSignupView(SignupView):
    """Overrides SignupView of the Allauth package"""
    template_name = 'account/signup.html'
    is_employer = False

    def dispatch(self, request, *args, **kwargs):
        """Setting signup redirect url for different types of users"""
        if request.POST.get('account_type') == 'employer':
            self.is_employer = True
            settings.ACCOUNT_SIGNUP_REDIRECT_URL = reverse('new_company')
        else:
            settings.ACCOUNT_SIGNUP_REDIRECT_URL = reverse('index_view')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Each user should have Userprofile depending on account type"""
        response = super().form_valid(form)
        user = self.request.user
        if self.is_employer:
            Userprofile.objects.create(user=user, is_employer=True)
        else:
            Userprofile.objects.create(user=user)
        return response
