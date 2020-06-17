from django import forms
from allauth.account.forms import LoginForm, SignupForm
import django_filters
from .models import Post, Contact,Story, Comment


class MyFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']


SITUATION = {
    ('D', 'Doctor'),
    ('P', 'Patient'),
}
class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=False, label="First Name")
    last_name = forms.CharField(max_length=50, required=False, label="Last Name")
    phone = forms.CharField(max_length=12, label='Phone')
    address = forms.CharField(max_length=100, label='Address', widget=forms.TextInput(attrs={'class':'flex-column'}))
    situation = forms.ChoiceField(label='Are You (Doctor/Patient)?', choices=SITUATION, widget=forms.RadioSelect())
    # img = forms.ImageField(upload_to='user_pics', required=False)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.situation = self.cleaned_data['situation']
        user.address = self.cleaned_data['address']
        user.save()
        return user

# class ContactForm(forms.Form):
#     model = Contact
#     fields = '__all__'

class AddStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = '__all__'
        exclude = {'user', 'slug', 'created','active'}

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = {'user', 'slug', 'created', 'active'}

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control w-100", 'placeholder':"Write Comment"}))
  