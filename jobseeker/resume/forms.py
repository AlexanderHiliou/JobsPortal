from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory

from jobseeker.resume.models import Resume, Education, Skill, WorkExperience


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = (
            'full_name', 'profile_picture', 'background_picture', 'headline', 'short_description', 'location', 'salary',
            'tags', 'phone', 'website', 'age', 'email', 'facebook_url', 'google_plus_url', 'dribbble_url',
            'pinterest_url', 'twitter_url', 'github_url', 'instagram_url', 'youtube_url')
        widgets={
        'full_name': forms.TextInput(attrs={
            'class': 'form-control input-lg',
            'placeholder': 'Full name'
        }),
        'headline': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Headline (e.g. Front-end developer)'
        }),
        'short_description': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Short description about you'
        }),
        'location': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Location, e.g. Melon Park, CA'
        }),
        'website': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Website address'
        }),
        'age': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Age'
        }),
        'salary': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Salary, e.g. 85'
        }),
        'tags': forms.TextInput(attrs={
            'placeholder': 'Tag name',
            'value': 'HTML,CSS,Javascript',
            'data-role': 'tagsinput'
        }),
        'phone': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone number',
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
        }),
        'facebook_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'google_plus_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'dribbble_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'pinterest_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'twitter_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'github_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'instagram_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        'youtube_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Profile URL',
        }),
        }


EducationFormSet = modelformset_factory(
    Education, fields=('academic_degree', 'school_logo', 'major', 'school', 'date_from', 'date_to', 'short_description'), extra=1,
    widgets={
        'academic_degree': forms.Select(attrs={
            'class': 'form-control',
        }),
        'school_logo': forms.FileInput(attrs={
            'class': 'dropify',
        }),
        'major': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Major, e.g. Computer Science'
        }),
        'school': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'School name, e.g. Massachusetts Institute of Technology'
        }),
        'date_from': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 2012'
        }),
        'date_to': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 2016'
        }),
        'short_description': forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Short description'
        }),
    }
)
ExperienceFormSet = modelformset_factory(
    WorkExperience, fields=('company_name', 'position', 'date_from', 'date_to', 'job_detail'), extra=1,
    widgets={
        'company_name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Company name'
        }),
        'position': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Position, e.g. UI/UX Researcher'
        }),
        'date_from': forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 10/25/2012'
        }),
        'date_to': forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 10/25/2016'
        }),
    }
)

SkillFormSet = modelformset_factory(
    Skill, fields=('name', 'proficiency'), extra=1,
    widgets={
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Skill name, e.g. HTML'
        }),
        'proficiency': forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Skill proficiency, e.g. 90'
        }),
    }
)

