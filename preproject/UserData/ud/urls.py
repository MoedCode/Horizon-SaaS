
from django.urls import path
from .views import *
urlpatterns = [
    path('user/create', UserCreate.as_view(), name='user-create'),
    path('user/register', UserRegister.as_view(), name='user-register'),
    path('user/image/<int:user_id>', UserImage.as_view(), name='user-image'),
    path('user/data/<int:user_id>', UserGetData.as_view(), name='user-data'),
    path('user/data/<str:name>', UserGetData.as_view(), name='user-data'),
    path('user/data/<int:user_id>/<str:name>', UserGetData.as_view(), name='user-data'),
    path('user/xpage', xPage.as_view(), name='x-page')
]