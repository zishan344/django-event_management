from django.urls import path
from users.views import Sign_up, Sign_in, Sign_out,activate_user,ChangeRole,updateRolePermission,deleteRole,CreateRoles,UserProfile

urlpatterns = [
    path('sign-up/',Sign_up, name="sign-up"),
    path('sign-in/',Sign_in, name="sign-in"),
    path('sign-out/',Sign_out, name="sign-out"),
    path('profile/',UserProfile.as_view(), name="profile"),
    path('activate/<int:user_id>/<str:token>/', activate_user,name='activate-user'),
    path('create-role/',CreateRoles.as_view(), name="create-role"),
    path('change-role/<int:user_id>/',ChangeRole,name="change-role"),
    path('update-rolePermission/<int:role_id>/',updateRolePermission,name="update-rolePermission"),
    path('role-delete/<int:role_id>/',deleteRole,name="role-delete"),
]