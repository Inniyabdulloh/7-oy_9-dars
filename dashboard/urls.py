from django.urls import path
from .views import ( HomeView, StaffLoginView,
        ServiceListView, ServiceDetailView, ServiceCreateView, ServiceDeleteView, ServiceUpdateView,
        PortfolioListView, PortfolioDetailView, PortfolioCreateView, PortfolioDeleteView, PortfolioUpdateView,
        StaffListView, StaffDetailView, StaffCreateView, StaffDeleteView, StaffUpdateView
                     )
from users import urls as user_urls


app_name = 'dashboard'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', StaffLoginView.as_view(), name='login'),

    path('services/list/', ServiceListView.as_view(), name='services-list'),
    path('services/create/', ServiceCreateView.as_view(), name='services-create'),
    path('services/detail/<int:id>/', ServiceDetailView.as_view(), name='services-detail'),
    path('services/delete/<int:id>/', ServiceDeleteView.as_view(), name='services-delete'),
    path('services/update/<int:id>/', ServiceUpdateView.as_view(), name='services-update'),

    path('portfolio/list/', PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolio/create/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('portfolio/detail/<int:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/delete/<int:id>/', PortfolioDeleteView.as_view(), name='portfolio-delete'),
    path('portfolio/update/<int:id>/', PortfolioUpdateView.as_view(), name='portfolio-update'),

    path('staff/list/', StaffListView.as_view(), name='staff-list'),
    path('staff/create/', StaffCreateView.as_view(), name='staff-create'),
    path('staff/detail/<int:id>/', StaffDetailView.as_view(), name='staff-detail'),
    path('staff/delete/<int:id>/', StaffDeleteView.as_view(), name='staff-delete'),
    path('staff/update/<int:id>/', StaffUpdateView.as_view(), name='staff-update'),

    path('review/list/', user_urls.ReviewListView.as_view(), name='review-list'),
    path('review/create/', user_urls.ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:id>/detail/', user_urls.ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:id>/update/', user_urls.ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:id>/delete/', user_urls.ReviewDeleteView.as_view(), name='review-delete'),

    path('contact/list/', user_urls.ContactListView.as_view(), name='contact-list'),
    path('contact/create/', user_urls.ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:id>/detail/', user_urls.ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:id>/update/', user_urls.ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:id>/delete/', user_urls.ContactDeleteView.as_view(), name='contact-delete'),

]