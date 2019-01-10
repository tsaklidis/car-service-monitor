from django.db.models import Max
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from csm.companies.models import Company
from csm.users.models import Owner
from csm.cars.models import Car


def is_manager(user):
    # also import 'redirect' from shortcuts
    # try:
    #     company = Company.objects.filter(manager__id=user.id).exists()
    #     return True
    # except Company.DoesNotExist:
    #     # return redirect('public:no_rights')
    #     return False

    company = Company.objects.filter(manager__id=user.id).exists()
    if company:
        return True
    return False


@login_required
@user_passes_test(is_manager, login_url='public:no_rights')
def home(request):
    company = Company.objects.get(manager__id=request.user.id)
    owners = Owner.objects.filter(company=company)
    cars = Car.objects.filter(owner__company=company)
    most_ex_car = cars.aggregate(Max('price'))
    most_tr_car = cars.aggregate(Max('kilometers'))
    # Attention: Lot of queries, slowing down homepage
    # TODO fix relations
    # max_cars = -1
    # most_cars_owner = ''
    # for ow in owners:
    #     if ow.owned_cars > max_cars:
    #         most_cars_owner = ow.full_name()

    data = {
        'owners': owners.count(),
        'cars': cars.count(),
        'most_ex_car': most_ex_car['price__max'],
        'most_tr_car': most_tr_car['kilometers__max'],
        'manager': company.manager,
        'company': company,
    }
    return render(request, 'panel/home.html', data)


@login_required
@user_passes_test(is_manager, login_url='public:no_rights')
def owners(request):
    company = Company.objects.get(manager__id=request.user.id)
    owners = Owner.objects.filter(company=company).order_by('created_on')
    data = {
        'owners': owners,
        'manager': company.manager,
        'company': company,
    }
    return render(request, 'panel/owners.html', data)


@login_required
@user_passes_test(is_manager, login_url='public:no_rights')
def cars(request):
    company = Company.objects.get(manager__id=request.user.id)
    cars = Car.objects.filter(company=company).order_by('brand')
    data = {
        'cars': cars,
        'manager': company.manager,
        'company': company,
    }
    return render(request, 'panel/cars.html', data)


@login_required
@user_passes_test(is_manager, login_url='public:no_rights')
def car_single(request, car_id=None):

    company = Company.objects.get(manager__id=request.user.id)
    try:
        car = Car.objects.get(company=company, id=car_id)
    except Car.DoesNotExist:
        car = Car.objects.filter(company=company).last()

    data = {
        'car': car,
        'manager': company.manager,
        'company': company,
    }
    return render(request, 'panel/car_single.html', data)
