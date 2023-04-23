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
    # category_files = files_doc.objects.filter(category = cat_s)
    context = { 'employer' : emp , 'file' : file,}
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
def uchebnyi_proces(request):
    return render(request, 'diploma/uchebnyi_proces.html')

@login_required(login_url='login')
def nauchno(request):
    return render(request, 'diploma/nauchno.html')

@login_required(login_url='login')
def vospitatel(request):
    return render(request, 'diploma/vospitatel.html')

@login_required(login_url='login')
def mezhdunarod(request):
    return render(request, 'diploma/mezhdunarod.html')

@login_required(login_url='login')
def personal(request):
    return render(request, 'diploma/personal.html')

@login_required(login_url='login')
def admin_hozyai(request):
    return render(request, 'diploma/admin_hoz.html')

def history(request):
    return render(request, 'diploma/archive.html')

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

@login_required(login_url='login')
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
    return render(request, 'diploma/results_page.html') 

@login_required(login_url='login')
@admin_only
def update_file(request, id):
    file = files_doc.objects.get(id=id)
    form = FilesForm(instance=file)
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
           form.save()
           return redirect('home')
    else :
        form = FilesForm()
    context = {'form': form}
    return render(request, 'diploma/update_files.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['users','admin'])
def read_file(request): 
    f = codecs.open('static/images/document/pdf/dz7_1_3.docx', mode='r', encoding='latin-1')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, 'diploma/view.html', context)


def categories(request, cat_s):
    category_files = files_doc.objects.filter(category = cat_s)
    context = {'cat_s': cat_s, 'category_files': category_files}
    return render(request, 'diploma/categories.html', context)