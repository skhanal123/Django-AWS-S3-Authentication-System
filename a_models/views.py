from django.shortcuts import render, HttpResponseRedirect
from .models import UniwareMaster, UniwareDimension, Inbound
from .forms import FormUniwareMaster, FormUniwareMaster1, FormUniwareDimension, EditProfileForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm
from .decorators import group_check

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request = request, data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect(reverse('profile'))
        else:
            fm = AuthenticationForm()
        return render(request, 'a_models/login.html', {'form': fm})
    else:
        return HttpResponseRedirect(reverse('login'))

@group_check(allowed_grps = ['HR'])
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditProfileForm(request.POST, instance = request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Updated Successfully')
        else:
            fm = EditProfileForm(instance = request.user)    
        return render(request, 'a_models/profile.html', {'name': str(request.user), 'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))

def user_changepassword1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect(reverse('profile'))
        else:
            fm = SetPasswordForm(user = request.user)    
        return render (request, 'a_models/passwordchange1.html', {'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))

def user_changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user = request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect(reverse('profile'))
        else:
            fm = PasswordChangeForm(user = request.user)    
        return render (request, 'a_models/passwordchange.html', {'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'a_models/signup.html', {'form':fm})


# Create your views here.
def uniware_master(request):
    products = UniwareMaster.objects.all()
    inbounds = Inbound.objects.all()
    return render(request, 'a_models/uniware.html', {'products': products, 'inbounds':inbounds})

def storeuniware(request):
    if request.method == 'POST':
        uni = FormUniwareMaster(request.POST, request.FILES)
        if uni.is_valid():
            uniware = uni.cleaned_data['uniware']
            brand = uni.cleaned_data['brand']
            headcat = uni.cleaned_data['headcat']
            subcat = uni.cleaned_data['subcat']
            productpic = uni.cleaned_data['productpic']
            input_data = UniwareMaster(uniware = uniware, brand = brand, headcat = headcat, subcat = subcat, productpic = productpic)
            input_data.save()
    else:
        uni = FormUniwareMaster()

    return render(request, 'a_models/form.html', {'uni': uni})

def storeuniware1(request):
    if request.method == 'POST':
        uni = FormUniwareMaster1(request.POST, request.FILES)
        if uni.is_valid():
            uniware = uni.cleaned_data['uniware']
            brand = uni.cleaned_data['brand']
            headcat = uni.cleaned_data['headcat']
            subcat = uni.cleaned_data['subcat']
            productpic = uni.cleaned_data['productpic']
            input_data = UniwareMaster(uniware = uniware, brand = brand, headcat = headcat, subcat = subcat, productpic = productpic)
            input_data.save()
    else:
        uni = FormUniwareMaster1()

    return render(request, 'a_models/form1.html', {'uni': uni})

def createandread(request):
    if request.method == 'POST':
        uni = FormUniwareDimension(request.POST)
        if uni.is_valid():
            uniware = uni.cleaned_data['uniware']
            length = uni.cleaned_data['length']
            width = uni.cleaned_data['width']
            height = uni.cleaned_data['height']
            
            input_data = UniwareDimension(uniware = uniware, length = length, width = width, height = height)
            input_data.save()
    else:
        uni = FormUniwareDimension()
    products = UniwareDimension.objects.all()

    return render(request, 'a_models/createandread.html', {'uni': uni, 'products': products})

def deletedata(request, id):
    if request.method == 'POST':
        product = UniwareDimension.objects.get(pk=id)
        product.delete()
        return HttpResponseRedirect(reverse('createandread'))

def updatedata(request, id):
    if request.method == 'POST':
        product = UniwareDimension.objects.get(pk=id)
        uni = FormUniwareDimension(request.POST, instance = product)
        if uni.is_valid():
            uni.save()
    else:
        product = UniwareDimension.objects.get(pk=id)
        uni = FormUniwareDimension(instance = product)
    return render(request, 'a_models/updatedata.html', {'uni': uni})

def messageconcept(request):
    if request.method == 'POST':
        uni = FormUniwareDimension(request.POST)
        if uni.is_valid():
            uniware = uni.cleaned_data['uniware']
            length = uni.cleaned_data['length']
            width = uni.cleaned_data['width']
            height = uni.cleaned_data['height']
            
            input_data = UniwareDimension(uniware = uniware, length = length, width = width, height = height)
            input_data.save()
            uni = FormUniwareDimension()
            messages.success(request, "Your data is saved!!")
            print(messages.get_level(request))
            messages.set_level(request, messages.DEBUG)
            messages.info(request, "You can now calculate space!!")
            
    else:
        uni = FormUniwareDimension()
    return render(request, 'a_models/messageconcept.html', {'uni': uni})

def forbidden(request):
    return render(request, 'a_models/forbidden.html')


