from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import Services, Portfolio, Staff
from users.models import Review, Contact
# Create your views here.

class HomeView(View):
    def get(self, request):
        contacts = Contact.objects.all().order_by('-id')
        context = {
            'contacts': contacts,
        }
        return render(request, 'dashboard/index.html', context)

class StaffLoginView(View):
    def get(self, request):
        return render(request, 'dashboard/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard:home')

        return redirect('dashboard:login')

class ServiceListView(View):
    def get(self, request):
        services = Services.objects.all()
        context = {'services': services}
        return render(request, 'dashboard/services/service_list.html', context)


class ServiceDetailView(View):
    def get(self, request, id):
        service = Services.objects.get(id=id)
        context = {'service': service}
        return render(request, 'dashboard/services/service_detail.html', context)


class ServiceCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/services/service_create.html')

    def post(self, request):
        try:
            Services.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
                icon=request.FILES['icon'],
            )

        except:
            ...

        return redirect('dashboard:services-list')


class ServiceUpdateView(View):
    def get(self, request, id):
        service = Services.objects.get(id=id)
        context = {'service': service}
        return render(request, 'dashboard/services/service_update.html', context)

    def post(self, request, id):
        service = Services.objects.get(id=id)
        service.name = request.POST['name']
        service.description = request.POST['description']
        service.icon = request.FILES['icon']
        service.save()

        return redirect('dashboard:services-detail', id=id)


class ServiceDeleteView(View):
    def get(self, request, id):
        service = Services.objects.get(id=id)
        service.delete()
        return redirect('dashboard:services-list')


class PortfolioListView(View):
    def get(self, request):
        portfolio = Portfolio.objects.all()
        context = {'portfolios': portfolio}
        return render(request, 'dashboard/portfolio/portfolio_list.html', context)


class PortfolioDetailView(View):
    def get(self, request, id):
        portfolio = Portfolio.objects.get(id=id)
        context = {'portfolio': portfolio}
        return render(request, 'dashboard/portfolio/portfolio_detail.html', context)


class PortfolioCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/portfolio/portfolio_create.html')

    def post(self, request):
        try:
            Portfolio.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
                image=request.FILES['image'],
            )
        except:
            ...

        return redirect('dashboard:portfolio-list')


class PortfolioUpdateView(View):
    def get(self, request, id):
        portfolio = Portfolio.objects.get(id=id)
        context = {'portfolio': portfolio}
        return render(request, 'dashboard/portfolio/portfolio_update.html', context)

    def post(self, request, id):
        portfolio = Portfolio.objects.get(id=id)
        portfolio.name = request.POST['name']
        portfolio.description = request.POST['description']
        try:
            portfolio.image = request.FILES['image']
        except:
            portfolio.image = portfolio.image
        portfolio.save()

        return redirect('dashboard:portfolio-detail', id=id)


class PortfolioDeleteView(View):
    def get(self, request, id):
        portfolio = Portfolio.objects.get(id=id)
        portfolio.delete()
        return redirect('dashboard:portfolio-list')



class StaffListView(View):
    def get(self, request):
        staff = Staff.objects.all()
        context = {'staff': staff}
        return render(request, 'dashboard/staff/staff_list.html', context)


class StaffDetailView(View):
    def get(self, request, id):
        staff = Staff.objects.get(id=id)
        context = {'staff': staff}
        return render(request, 'dashboard/staff/staff_detail.html', context)


class StaffCreateView(View):
    def get(self, request):
        return render(request, 'dashboard/staff/staff_create.html')

    def post(self, request):
        try:
            Staff.objects.create(
                full_name=request.POST['full_name'],
                specialty=request.POST['specialty'],
                bio=request.POST['bio'],
                image=request.FILES['image'],
                twitter=request.POST['twitter'],
                facebook=request.POST['facebook'],
                instagram=request.POST['instagram'],
                linkedin=request.POST['linkedin'],
            )


        except:
            ...

        return redirect('dashboard:staff-list')


class StaffUpdateView(View):
    def get(self, request, id):
        staff = Staff.objects.get(id=id)
        context = {'staff': staff}
        return render(request, 'dashboard/staff/staff_update.html', context)

    def post(self, request, id):
        staff = Staff.objects.get(id=id)
        staff.full_name = request.POST['full_name']
        staff.bio = request.POST['bio']
        staff.specialty = request.FILES['specialty']
        if request.FILES.get('image'):
            staff.image = request.FILES['image']
        else:
            staff.image = staff.image

        staff.save()

        return redirect('dashboard:staff-detail', id=id)


class StaffDeleteView(View):
    def get(self, request, id):
        staff = Staff.objects.get(id=id)
        staff.delete()
        return redirect('dashboard:staff-list')
