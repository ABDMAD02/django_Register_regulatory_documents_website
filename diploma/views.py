from django.shortcuts import render, redirect
from .forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import employer
from .models import files_doc
from .models import Category
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import EmployerForm, FilesForm, choices
import codecs


# if request.user.is_authenticated:
#     return redirect('home')
# else:

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','users'])
def welcome(request):
    emp = employer.objects.all()
    file = files_doc.objects.all()
    category_list = Category.objects.all()
    context = { 'employer' : emp , 'file' : file, 'category_list': category_list} 
    return render(request, 'diploma/index.html', context)

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
    category_list = Category.objects.all()
    if request.user.is_staff:
        admin = request.user
        context = {'admin' : admin, 'category_list': category_list}
        return render(request, 'diploma/profile.html',context)
    else:
        emp = request.user.employer
        context = {'employer' : emp, 'category_list': category_list} 
        return render(request, 'diploma/profile.html',context)

# @login_required(login_url='login')
# def upload_files(request):
#     return render(request, 'diploma/upload_files')

def history(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'diploma/archive.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','users'])
def acc_settings(request):
    category_list = Category.objects.all()
    if request.user.is_staff:
        context = {'category_list': category_list}
        return render(request, 'diploma/acc_settings.html', context)
    else:
        employer = request.user.employer
        form = EmployerForm(instance=employer)
        if request.method == 'POST':
            form = EmployerForm(request.POST, request.FILES, instance=employer)
            if form.is_valid():
                form.save()
        context = {'form': form, 'category_list': category_list}
        return render(request, 'diploma/acc_settings.html', context)

@login_required(login_url='login')
@admin_only
def file_up(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('home')
    else :
        form = FilesForm() 
    context = {'form':form, 'category_list': category_list}
    return render(request, 'diploma/upload_files.html', context)

@login_required(login_url='login')
@admin_only
def delete_file(request, pk):
    if request.method == 'POST':
        fileDelete = files_doc.objects.get(pk=pk)
        fileDelete.delete()
    return redirect('home')

@login_required(login_url='login')
@allowed_users(allowed_roles=['users','admin'])
def results(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    if request.method == 'POST':
        searched = request.POST.get('searched')
        files = files_doc.objects.filter(topic__contains = searched)
        context = {'category_list': category_list, 'searched': searched, 'files': files}
        return render(request, 'diploma/results_page.html', context)     
    else :
        return render(request, 'diploma/results_page.html', context) 

@login_required(login_url='login')
@admin_only
def update_file(request, id):
    category_list = Category.objects.all()
    file = files_doc.objects.get(id=id)
    form = FilesForm(instance=file)
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
           form.save()
           return redirect('home')
    else :
        form = FilesForm()
    context = {'form': form, 'category_list': category_list}
    return render(request, 'diploma/update_files.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['users','admin'])
# def read_file(request): 
#     f = codecs.open('static/images/document/pdf/dz7_1_3.docx', mode='r', encoding='latin-1')
#     file_content = f.read()
#     f.close()
#     context = {'file_content': file_content}
#     return render(request, 'diploma/view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['users','admin'])
def categories(request, cat_s):
    category_list = Category.objects.all()
    category_files = files_doc.objects.filter(category = cat_s)
    context = {'cat_s': cat_s, 'category_files': category_files, 'category_list': category_list}
    return render(request, 'diploma/categories.html', context)