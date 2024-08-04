from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import User, Review, Contact
from dashboard.models import Services, Portfolio, Staff
# Create your views here.

class HomePageView(View):
    def get(self, request):
        services = Services.objects.all()
        portfolios = Portfolio.objects.all()
        staff = Staff.objects.all()
        reviews = Review.objects.all()
        context = {
            'services': services, 'portfolios': portfolios,
            'staff': staff, 'reviews': reviews
        }

        return render(request, 'users/index.html', context)


class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('users:home')

        return redirect('users:login')





class ReviewListView(View):
     def get(self, request):
         if request.user.is_staff:
             reviews = Review.objects.all()
         else:
             reviews = Review.objects.filter(user=request.user)
         context = {'reviews': reviews}
         return render(request, 'users/review/review_list.html', context)


class ReviewDetailView(View):
    def get(self, request, id):
        review = Review.objects.get(id=id)
        context = {'review': review}
        return render(request, 'users/review/review_detail.html', context)


class ReviewCreateView(View):
    def get(self, request):

        return render(request, 'users/review/review_create.html')

    def post(self, request):
        Review.objects.create(
            user=request.user,
            speciality=request.POST['speciality'],
            review=request.POST['review'],
            stars_given=int(request.POST['stars']),
        )
        return redirect('users:review-list')
class ReviewUpdateView(View):
    def get(self, request, id):
        review = Review.objects.get(id=id)
        context = {'review': review}
        return render(request, 'dashboard/review/review_update.html', context)

    def post(self, request, id):
        review = Review.objects.get(id=id)
        review.review = request.POST['review']
        review.speciality = request.POST['speciality']
        review.stars_given = int(request.POST['stars'])
        review.save()

        return redirect('users:review-detail', id=review.id)


class ReviewDeleteView(View):
     def get(self, request, id):
         review = Review.objects.get(id=id)
         review.delete()

         return redirect('users:review-list')




class ContactListView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        context = {'contacts': contacts}
        return render(request, 'dashboard/contact/contact_list.html', context)


class ContactDetailView(View):
    def get(self, request, id):
        contact = Contact.objects.get(id=id)
        context = {'contact': contact}
        return render(request, 'dashboard/contact/contact_detail.html', context)


class ContactCreateView(View):
    def post(self, request):
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )

        return redirect('users:home')

class ContactUpdateView(View):
    def get(self, request, id):
        contact = Contact.objects.get(id=id)
        context = {'contact': contact}
        return render(request, 'dashboard/contact/contact_update.html', context)

    def post(self, request, id):
        contact = Contact.objects.get(id=id)
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.save()

        return redirect('users:contact-detail', id=contact.id)


class ContactDeleteView(View):
    def get(self, request, id):
        contact = Contact.objects.get(id=id)
        contact.delete()

        return redirect('users:contact-list')