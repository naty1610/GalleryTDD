from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('publicPortfolio/<int:id>', views.portfolio_public_view, name='publicPortfolio'),
    path('loginUser/', views.login_view, name='loginUser'),
]
