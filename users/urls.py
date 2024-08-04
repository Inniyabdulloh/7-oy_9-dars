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
   path('review/<int:id>/detail/', ReviewDetailView.as_view(), name='review-detail'),
   path('review/<int:id>/update/', ReviewUpdateView.as_view(), name='review-update'),
   path('review/<int:id>/delete/', ReviewDeleteView.as_view(), name='review-delete'),

   path('contact/list/', ContactListView.as_view(), name='contact-list'),
   path('contact/create/', ContactCreateView.as_view(), name='contact-create'),
   path('contact/<int:id>/detail/', ContactDetailView.as_view(), name='contact-detail'),
   path('contact/<int:id>/update/', ContactUpdateView.as_view(), name='contact-update'),
   path('contact/<int:id>/delete/', ContactDeleteView.as_view(), name='contact-delete'),

]

