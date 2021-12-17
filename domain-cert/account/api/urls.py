from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView 

app_name = 'cert'   # 指定命名空间

urlpatterns = [
    path('login/', views.TokenObtainPairView .as_view(), name='token_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(r'account/user', views.UserListView.as_view(), name='user_list'),
    path(r'account/user/<pk>', views.UserDetailView.as_view(), name='user_detail'),
    path(r'account/role', views.RoleListView.as_view(), name='role_list'),
    path(r'account/role/<pk>', views.RoleDetailView.as_view(), name='role_detail'),
    path(r'account/structure', views.StructureListView.as_view(), name='structure_list'),
    path(r'account/structure/<pk>', views.StructureDetailView.as_view(), name='structure_detail'),
    path('account/changepasswd/', views.ChangePasswd.as_view(), name='passwd'),
    path('account/username/', views.UsernameView.as_view(), name='username'),
    path('account/permlist/', views.PermsView.as_view(), name='perm'),
    path('account/userinfo/', views.UserProfileView.as_view(), name='user_info'),
]