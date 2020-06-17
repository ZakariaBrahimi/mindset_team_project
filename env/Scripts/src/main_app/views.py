from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Contact, Comment, Story, Appointment
from .forms import MyFilter, AddStory, AddPost, CommentForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib import messages
# from next_prev import next_in_order, prev_in_order
def blog(request):
    # user= request.user
    posts = Post.objects.all()
    filter = MyFilter(request.GET, queryset=posts)
    posts = filter.qs
    #<<---------------------------------Pagination--------------------------------------------------------------->>
    p = Paginator(posts, 4)
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
login_required(login_url='account_login')
def add_story(request):
    if request.method == 'POST':
        form = AddStory(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'You added a story successfuly.')
            return redirect('main:share_stories')
    else:
        form = AddStory()
    context = {'form' : form,}
    return render(request, 'add_story.html', context)

login_required(login_url='account_login')
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'You added an article successfuly.')
            return redirect('main:blog')
    else:
        form = AddPost()
    context = {'form' : form,}
    return render(request, 'add_post.html', context)

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        typee = request.POST.get('typee')
        time = request.POST.get('time')
        text = request.POST.get('text')
        Appointment(name=name,email=email,time=time, typee=typee, text=text).save()
        messages.success(request, 'Your Appointment has been Succeeded, Waiting for Email confirmation.')
        return redirect('/')
    context = {}
    return render(request, 'index.html', context)


def one_story(request, story_slug, story_id):
    story = get_object_or_404(Story, slug=story_slug, pk=story_id)
    # next_story = next_in_order(story)
    comments = Comment.objects.filter(story=story)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            co = Comment(comment=comment).save()
            story.comments = co
            story.save()
            return redirect('main:one_story', story_id, story_slug)
    else:
        form = CommentForm()
    context = {
        'story' : story,
        'form' : form,
        # 'next_story' : next_story,
    }
    return render(request, 'one_story.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def doctors(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        typee = request.POST.get('typee')
        time = request.POST.get('time')
        text = request.POST.get('text')
        Appointment(name=name,email=email,time=time, typee=typee, text=text).save()
        messages.success(request, 'Your Appointment has been Succeeded, Waiting for Email confirmation.')
        return redirect('main:doctors')
    context = {}
    return render(request, 'doctor.html', context)

def duasreminders(request):
    context = {}
    return render(request, 'duasreminders.html', context)


def share_stories(request):
    stories = Story.objects.all()
    filter = MyFilter(request.GET, queryset=stories)
    stories = filter.qs
    p = Paginator(stories, 4)
    page = request.GET.get('page')

    try:
        stories = p.page(page)
    except PageNotAnInteger:
        stories = p.page(1)
    except EmptyPage:
        stories = p.num_pages
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment(comment=comment).save()
        return redirect('/')
    context = {
        'stories' : stories,
        'filter' : filter,
        'page' : page,
    }
    return render(request, 'shared_stories.html', context)
def contact(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        Contact(msg=msg,name=name,email=email,subject=subject).save()
        messages.info(request, 'We will get in touch to you.')
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



