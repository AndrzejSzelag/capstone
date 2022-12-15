from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # ======== Register & Login =======
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    # ======== C R U D =======
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('read/<int:pk>', views.ProjectReadView.as_view(), name='read'),
    path('update/<int:pk>', views.ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ProjectDeleteView.as_view(), name='delete'),
]
