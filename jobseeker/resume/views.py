from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView

from jobseeker.resume.forms import ResumeForm, EducationFormSet, SkillFormSet, ExperienceFormSet
from jobseeker.resume.models import Education, WorkExperience, Skill

from jobseeker.resume.models import Resume


class ResumeCreateView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    # template_name = "resume/resume-add.html"

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        form = ResumeForm()
        education_formset = EducationFormSet(queryset=Education.objects.none(), prefix='education')
        experience_formset = ExperienceFormSet(queryset=WorkExperience.objects.none(), prefix='expirience')
        skill_formset = SkillFormSet(queryset=Skill.objects.none(), prefix='skill')
        return self.render_to_response(
            {'form': form, 'education_formset': education_formset, 'experience_formset': experience_formset,
             'skill_formset': skill_formset})

    def post(self, *args, **kwargs):
        form = ResumeForm(self.request.POST, self.request.FILES)
        education_formset = EducationFormSet(self.request.POST, self.request.FILES, prefix='education')
        experience_formset = ExperienceFormSet(self.request.POST, prefix='expirience')
        skill_formset = SkillFormSet(self.request.POST, prefix='skill')
        if form.is_valid() and education_formset.is_valid \
                and experience_formset.is_valid() and skill_formset.is_valid():
            resume = form.save(commit=False)
            resume.jobseeker = self.request.user.userprofile
            resume.slug = slugify(f'{resume.headline}-{resume.full_name}')
            resume.save()
            form.save_m2m()
            experience = experience_formset.save(commit=False)
            for exp in experience:
                exp.resume = Resume.objects.get(id=resume.id)
                exp.save()
            education = education_formset.save(commit=False)
            for form in education:
                form.resume = Resume.objects.get(id=resume.id)
                form.save()
            skills = skill_formset.save(commit=False)
            for skill in skills:
                skill.resume = Resume.objects.get(id=resume.id)
                skill.save()
            return redirect('/')
        return self.render_to_response(
            {'form': form, 'education_formset': education_formset, 'experience_formset': experience_formset,
             'skill_formset': skill_formset}
        )

    def test_func(self):
        """ Access is allowed only for Jobseekers  """
        user_is_employer = self.request.user.userprofile.is_employer
        if user_is_employer:
            return False
        return True
