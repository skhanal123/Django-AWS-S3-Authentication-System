from django.urls import path
from . import views

urlpatterns = [
    path('model', views.uniware_master, name='uniware_master'),
    path('modelform', views.storeuniware, name='modelform_concept'),
    path('formapi', views.storeuniware1, name='formapi_concept'),
    path('createandread', views.createandread, name='createandread'),
    path('deletedata/<int:id>/', views.deletedata, name='deletedata'),
    path('<int:id>/', views.updatedata, name='updatedata'),
    path('messageconcept', views.messageconcept, name='messageconcept'),
    path('signup', views.signup, name='userauthentication'),
    path('login', views.user_login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.user_logout, name='logout'),
    path('changepassword', views.user_changepassword, name='changepassword'),
    path('changepassword1', views.user_changepassword1, name='changepassword1'),
    path('forbidden', views.forbidden, name='forbidden'),
    
]