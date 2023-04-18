from django.shortcuts import render, redirect
from .forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import example
from .models import employer
from .models import pdf_files
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import EmployerForm, FilesForm

# if request.user.is_authenticated:
#     return redirect('home')
# else:

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','users'])
def welcome(request):
    emp = employer.objects.all()
    file = pdf_files.objects.all()
    context = { 'employer' : emp , 'file' : file}
    return render(request, 'diploma/index.html', context)

@login_required(login_url='login')
def pat(request):
    return render(request, 'diploma/pattern.html')

@unauthenticated_user
def logPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect!')

    context = {}    
    return render(request, 'diploma/login.html', context)

def LogOut(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def reg(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'users')
            user.groups.add(group)
            employer.objects.create(
                user = user,
                name = user.username,
                email = user.email,
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form' : form }
    return render(request, 'diploma/registration.html', context)
 
@login_required(login_url='login')
@allowed_users(allowed_roles=['users','admin'])
def profile(request):
    if request.user.is_staff:
        admin = request.user
        context = {'admin' : admin}
        return render(request, 'diploma/profile.html',context)
    else:
        emp = request.user.employer
        context = {'employer' : emp} 
        return render(request, 'diploma/profile.html',context)

# @login_required(login_url='login')
# def upload_files(request):
#     return render(request, 'diploma/upload_files')

@login_required(login_url='login')
def politika(request):
    return render(request, 'diploma/politika.html')

@login_required(login_url='login')
def organ_i_rek(request):
    return render(request, 'diploma/o_rektore.html')

@login_required(login_url='login')
def suggestion(request):
    return render(request, 'diploma/recomendacii.html')

@login_required(login_url='login')
def pravilaa(request):
    return render(request, 'diploma/pravila.html')

@login_required(login_url='login')
def procedura(request):
    return render(request, 'diploma/procedura.html')

@login_required(login_url='login')
def vnutrii(request):
    return render(request, 'diploma/vnd.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','users'])
def acc_settings(request):
    if request.user.is_staff:
        context = {}
        return render(request, 'diploma/acc_settings.html', context)
    else:
        employer = request.user.employer
        form = EmployerForm(instance=employer)
        if request.method == 'POST':
            form = EmployerForm(request.POST, request.FILES, instance=employer)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'diploma/acc_settings.html', context)


@admin_only
def file_up(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('home')
    else :
        form = FilesForm()
    context = {'form':form}
    return render(request, 'diploma/upload_files.html', context)

@admin_only
def delete_file(request, pk):
    if request.method == 'POST':
        fileDelete = pdf_files.objects.get(pk=pk)
        fileDelete.delete()
    return redirect('home')