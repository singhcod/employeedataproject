from django.shortcuts import render,redirect
from django.http import HttpResponse
import faker
fake = faker.Faker()
from .models import EmployeeData
from.forms import CreateUserForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def register_view(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)  # take form data
            if form.is_valid():
                form.save()
                return redirect('login')  # use redirect for go to another views
            else:
                form = CreateUserForm()
                return render(request, 'register.html', {'form': form})
        else:
            form = CreateUserForm()
            return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == "POST":
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')
            user = authenticate(username=username1, password=password1)
            if user is not None:
                login(request, user)
                messages.success(request, 'Hi you have login successfully')
                return redirect('home_page')
            else:
                messages.warning(request, 'Invalid user or password')
                return redirect('login')
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request,'Logout successfully')
    return redirect('login')


def employeedata_view(request):
    for i in range(500):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address = fake.address()
        salary = fake.random_element(elements = (10000,30000,20000,25000,35000))
        job = fake.random_element(elements = ('Govt','Private','Finance','Teaching','Marketing'))
        company = fake.random_element(elements = ('TCS','NTH','Wipro','Infosys','CTS'))
        location = fake.random_element(elements = ('Hyderabad','Bangalore','Chennai','Pune','Delhi'))

        EmployeeData(
            first_name = first_name,
            last_name = last_name,
            salary = salary,
            email = email,
            address = address,
            job = job,
            company = company,
            location = location
        ).save()
    return HttpResponse('Data Saved')


def fetching_data(request):
    employees = EmployeeData.objects.all()    #take data from browser
    return render(request,'allemployeesdata.html',{'employees':employees})



@login_required(login_url='login')
def home_page(request):
    return render(request,'home_page.html')


@login_required(login_url='login')
def hyderabad_data(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        hyd_data = EmployeeData.objects.filter(Q(location = 'Hyderabad'))& EmployeeData.objects.filter(company = company)
        return render(request,'hyd_data.html',{'employees':hyd_data})

    else:
        hyd_data = EmployeeData.objects.filter(location = 'Hyderabad')
        return render(request,'hyd_data.html',{'employees':hyd_data})
   
@login_required(login_url='login')
def bangalore_data(request):
    if request.method == 'POST':
       company = request.POST.get('company')
       bang_data = EmployeeData.objects.filter(Q(location = 'Bangalore') & Q(company = company))
       return render(request,'bang_data.html',{'employees':bang_data})
    else:
        bang_data = EmployeeData.objects.filter(location = 'Bangalore')
        return render(request,'bang_data.html',{'employees':bang_data})
@login_required(login_url='login')
def chennai_data(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        chennai_data = EmployeeData.objects.filter(location = 'Chennai') & EmployeeData.objects.filter(company = company)
        return render(request,'chennai_data.html',{'employees':chennai_data})
    else:
        chennai_data = EmployeeData.objects.filter(location = 'Chennai')
        return render(request,'chennai_data.html',{'employees':chennai_data})

@login_required(login_url='login')
def pune_data(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        pune_data = EmployeeData.objects.filter(location = 'Pune') & EmployeeData.objects.filter(comapny = company)
        return render(request,'pune_data.html',{'employees':pune_data})
    else:
        pune_data = EmployeeData.objects.filter(location = 'Pune')
        return render(request,'pune_data.html',{'employees':pune_data})

@login_required(login_url='login')
def delhi_data(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        delhi_data = EmployeeData.objects.filter(location = 'Delhi') & EmployeeData.objects.filter(company = company)
        return render(request,'delhi_data.html',{'employees':delhi_data})
    else:
        delhi_data = EmployeeData.objects.filter(location = 'Delhi')
        return render(request,'delhi_data.html',{'employees': delhi_data})





    
    
    
    