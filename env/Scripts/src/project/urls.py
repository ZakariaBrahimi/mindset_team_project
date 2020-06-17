from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('', include('main_app.urls',namespace='main')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# S = input()
# print(any([char.isalnum() for char in S]))
# print(any([char.isalpha() for char in S]))
# print(any([char.isdigit() for char in S]))
# print(any([char.islower() for char in S]))
# print(any([char.isupper() for char in S]))
# for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
#     print any(method(c) for c in s)
# or
# t = type(s)
# for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
#     print any(method(c) for c in s)