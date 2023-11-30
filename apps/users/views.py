from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib import messages

from apps.users.models import User, Settings



def register(request):
    current_date = datetime.now()
    setting = Settings.objects.latest('id')
    # temperature, weather_condition = get_weather_data()

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')
        if len(password) < 8:
            messages.error(request, 'Пароль должен быть не менее 8 символов')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует')
            return redirect('register')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=firstname,
            last_name=lastname,
            surname=surname
        )
        user.save()
        user_login = authenticate(username=email, password=password)
        login(request, user_login)

        messages.success(request, 'Вы успешно зарегистрированы. Теперь вы можете войти.')

        return redirect('/')
      
    return render(request, 'users/register.html', locals())

def user_login(request):
    setting = Settings.objects.latest('id')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему.')
            return redirect('/')
        else:
            messages.error(request, 'Неправильный email или пароль.')
            return redirect('login')
    
    return render(request, 'users/login.html', locals())

def profile(request,id):
    setting = Settings.objects.latest('id')
    user = User.objects.get(id=id)
    if request.method == "POST":
        if 'update_account' in request.POST:
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            user.first_name = first_name
            user.phone = phone
            user.email = email
            user.address = address
            user.save()
            return redirect('profile', request.user.id)
        if 'change_password' in request.POST:
            old_password = request.POST['old_password']
            new_password1 = request.POST['new_password1']
            new_password2 = request.POST['new_password2']
            user = request.user

            # Проверяем, совпадает ли введенный старый пароль с текущим паролем пользователя
            if user.check_password(old_password):
                # Проверяем, совпадают ли новые пароли
                if new_password1 == new_password2:
                    # Устанавливаем новый пароль
                    user.set_password(new_password1)
                    user.save()
                    
                    # Авторизуем пользователя с новым паролем
                    user = authenticate(firstname=user.firstname, password=new_password1)
                    if user:
                        login(request, user)

                    messages.success(request, 'Пароль успешно изменен.')
        if 'profile_images' in request.POST:
            firstname = request.POST.get('firstname')
            profile_image = request.FILES.get('profile_image')
            user.firstname = firstname
            user.profile_image = profile_image
            user.save()
            return redirect('profile', request.user.id)
    return render(request, 'users/settings-profile.html', locals())

def get_latest_settings():
    return Settings.objects.latest('id')

