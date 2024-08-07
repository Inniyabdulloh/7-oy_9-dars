from django.urls import path
from . import views
urlpatterns = [
    # user
    path('user/create/', views.UserView.as_view()),
    path('users/<int:pk>/detail/', views.UserView.as_view()),
    path('users/<int:pk>/update/', views.UserView.as_view()),
    path('users/<int:pk>/delete/', views.UserView.as_view()),

    # portfolio
    path('portfolio/list/', views.PortfolioView.as_view()),
    path('portfolio/create/', views.PortfolioView.as_view()),
    path('portfolio/<int:pk>/update/', views.PortfolioView.as_view()),
    path('portfolio/<int:pk>/delete/', views.PortfolioView.as_view()),

    # servise
    path('servise/list/', views.ServiseView.as_view()),
    path('servise/create/', views.ServiseView.as_view()),
    path('servise/<int:pk>/update/', views.ServiseView.as_view()),
    path('servise/<int:pk>/delete/', views.ServiseView.as_view()),

    # staff
    path('staff/list/', views.StaffView.as_view()),
    path('staff/create/', views.StaffView.as_view()),
    path('staff/<int:pk>/update/', views.StaffView.as_view()),
    path('staff/<int:pk>/delete/', views.StaffView.as_view()),

    # contact
    path('contact/list/', views.ContactView.as_view()),
    path('contact/create/', views.ContactView.as_view()),
    path('contact/<int:pk>/update/', views.ContactView.as_view()),
    path('contact/<int:pk>/delete/', views.ContactView.as_view()),
]