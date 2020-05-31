from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Contact
from .forms import MyFilter
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def blog(request):
    # user= request.user
    posts = Post.objects.all()
    filter = MyFilter(request.GET, queryset=posts)
    posts = filter.qs
    #<<---------------------------------Pagination--------------------------------------------------------------->>
    p = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = p.page(page)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.num_pages

    context = {
        'posts' : posts,
        'filter' : filter,
        'page' : page,
    }
    return render(request, 'blog.html', context)

def home(request):
    
    context = {}
    return render(request, 'index.html', context)
# Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def doctors(request):
    context = {}
    return render(request, 'doctor.html', context)

def duasreminders(request):
    context = {}
    return render(request, 'duasreminders.html', context)


def share_stories(request):  
    context = {}
    return render(request, 'shared_stories.html', context)

def contact(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Contact(msg=msg,name=name,email=email,subject=subject).save()
        return redirect('/')
    context = {}
    return render(request, 'contact.html', context)

def funactivities(request):
    context = {}
    return render(request, 'funactivities.html', context)





#<<===============================================during developement=====================================================>>
# def blog(request):
#     # user= request.user
#     # profile = get_object_or_404(Profile, user = user)
#     posts = Post.objects.all()
#     filter = MyFilter(request.GET, queryset=posts)
#     posts = filter.qs
#     #<<---------------------------------Pagination--------------------------------------------------------------->>
#     p = Paginator(home_notes, 6,orphans=1)
#     page = request.GET.get('page')
#     try:
#         posts = p.page(page)
#     except PageNotAnInteger:
#         posts = p.page(1)
#     except EmptyPage:
#         posts = p.num_pages

#     context = {
#         'home_notes' : home_notes,
#         # 'profile' : profile,
#         'filter' : filter,
#         'page' : page,
#     }
#     return render(request, 'blog.html', context)

# def post_detial(request, slug, one_post_id):
#     user = request.user
#     # profile = get_object_or_404(Profile, user = user)
#     one_post = Post.objects.get(slug=slug, pk=one_post_id)
#     context = {
#         'one_post' : one_post,
#         # 'profile' : profile,
#     }
#     return render(request, 'one_note.html', context)
#<<===============================================fin=====================================================>>



# def contact(request):
#     if request.method == 'POST':
#         textform = ContactForm()
#         if textform.is_valid():
#             textform.save()
#             return redirect('/')
#     else:
#         textform = ContactForm()
#     context = {
#         'textform' : textform,
#         }
#     return render(request, 'contact.html', context)

# class DoctorSignup(SignupView):
#     template_name = 'doctor_signup.html'
#     form_class = DoctorSignupForm
#     redirect_field_name = 'next'
#     # view_name = 'candidate_sign_up'

#     def get_context_data(self, **kwargs):
#         ret = super(DoctorSignup, self).get_context_data(**kwargs)
#         ret.update(self.kwargs)
#         return ret



