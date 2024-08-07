from django.urls import path
from .views import ( HomePageView, UserLoginView,
         ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView,
         ContactListView, ContactCreateView, ContactDetailView, ContactUpdateView, ContactDeleteView
                     )

app_name = 'users'

urlpatterns = [
   path('', HomePageView.as_view(), name='home'),
   path('login/', UserLoginView.as_view(), name='login'),

   path('review/list/', ReviewListView.as_view(), name='review-list'),
   path('review/create/', ReviewCreateView.as_view(), name='review-create'),

   path('contact/list/', ContactListView.as_view(), name='contact-list'),
   path('contact/create/', ContactCreateView.as_view(), name='contact-create'),

]

