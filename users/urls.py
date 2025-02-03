from django.urls import path
from users.views import Sign_up, Sign_in, Sign_out,activate_user

urlpatterns = [
    path('sign-up/',Sign_up, name="sign-up"),
    path('sign-in/',Sign_in, name="sign-in"),
    path('sign-out/',Sign_out, name="sign-out"),
    path('activate/<int:user_id>/<str:token>/', activate_user,name='activate-user'),
]