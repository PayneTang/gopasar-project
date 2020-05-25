from django.urls import path, include
from .api import LoginAPI, RegisterAPI, get_user, update_user, list_all_users, retrieve_user, check_user
from knox import views as knox_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('knox.urls')),

    path('user/register', RegisterAPI.as_view()),
    path('user/login', LoginAPI.as_view()),
    path('user/logout', knox_views.LogoutView.as_view(), name="knox_logout"),

    path('user/all', list_all_users),
    path('user/check', check_user),
    path('user/update', update_user),
    path('user/<str:pk>', get_user),
    path('user/', retrieve_user),
]
