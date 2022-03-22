from django.urls import path, include

print('vvvvvvvvvv')
urlpatterns = [
    path('blog_admin/', include('blog_admin.urls')),
]