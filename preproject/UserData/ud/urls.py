
from django.urls import path
from .views import *
urlpatterns = [
    path('user/create', UserCreate.as_view(), name='user-create'),
    path('user/register', UserRegister.as_view(), name='user-register'),
    path('user/image/', UserImage.as_view(), name='user-image'),
    path('user/data/', UserGetData.as_view(), name='user-data'),
    path('user/xpage', xPage.as_view(), name='x-page'),
    path('user/header', HeaderPage.as_view(), name='header'),
]