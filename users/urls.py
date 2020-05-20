from django.urls import path, include
from .api import UserAPI, CheckUserAPI, UserListAPI, LoginAPI, RegisterAPI
from knox import views as knox_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('knox.urls')),
    path('user/', UserAPI.as_view()),
    path('user/check', CheckUserAPI.as_view()),
    path('user/all', UserListAPI.as_view()),
    path('user/register', RegisterAPI.as_view()),
    path('user/login', LoginAPI.as_view()),
    path('user/logout', knox_views.LogoutView.as_view(), name="knox_logout"),
]
