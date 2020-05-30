from django import forms
from allauth.account.forms import LoginForm, SignupForm
import django_filters
from .models import Post


class MyFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title', 'tags']


SITUATION = {
    ('D', 'Doctor'),
    ('P', 'Patient'),
}
class MyCustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=12, label='Phone')
    situation = forms.ChoiceField(choices=SITUATION)
    address = forms.CharField(max_length=100, label='Address')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.situation = self.cleaned_data['situation']
        user.address = self.cleaned_data['address']
        user.save()
        return user
