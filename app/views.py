from django.shortcuts import render
from .models import Company, Product, Student, Course
from django.http import HttpResponseRedirect, HttpResponseNotFound
from datetime import date


# give info
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products' : products})

# add info to db
def create(request):
    create_companies()

    if request.method == 'POST':
        product = Product()
        product.name = request.POST.get('name')
        product.price = request.POST.get('name')
        product.company_id = request.POST.get('company')
        product.save()
        return HttpResponseRedirect('/')

    # передаём данные в шаблон
    companies = Company.objects.all()
    return render(request, 'create.html', {'companies': companies})

# edit db

def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.company_id = request.POST.get('company')
            product.save()
            return HttpResponseRedirect('/')
        else:
            companies = Company.objects.all()
            return render(request, 'edit.html', {"product": product, 'companies': companies})
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

# remove DB

def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

# add first values to table of companies

def create_companies():

    if Company.objects.all().count() == 0:
        Company.objects.create(name = 'Apple')
        Company.objects.create(name='Asus')
        Company.objects.create(name='MSI')

def index_many(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def create_many(request):
    initialize()

    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        course_ids = request.POST.detalis('courses')
        student.save()
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses, through_defaults={'date': date.today(), 'mark': 0})
        return HttpResponseRedirect("/")

    courses = Course.objects.all()
    return render(request, 'create_many.html', {'courses': courses})

def initialize():
    if Course.objects.all().count() == 0:
        Course.objects.create(name = 'Python')
        Course.objects.create(name=' Django')
        Course.objects.create(name= 'Fastapi')
