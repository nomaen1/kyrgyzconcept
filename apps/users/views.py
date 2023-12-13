from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from datetime import datetime
from django.contrib import messages

from apps.users.models import User, Settings
from apps.jobs.models import CV, ReadyCV



def register(request):
    setting = Settings.objects.latest('id')

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
            messages.error(request, 'Пароль должен состоять из букв и цифр')
            return redirect('register')

        valid_email_formats = ['gmail', 'email', 'icloud']
        if not any(format in email for format in valid_email_formats):
            messages.error(request, 'Неверный формат почты')
            return redirect('register')

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
            return redirect('/')
        else:
            messages.error(request, 'Неправильный email или пароль.')
            return redirect('login')
    
    return render(request, 'users/login.html', locals())
    
@login_required(login_url="login")
def profile(request, id):
    setting = Settings.objects.latest('id')
    user = User.objects.get(id=id)

    try:
        cv = CV.objects.get(user=request.user)
    except:
        pass

    try:
        ready_cv = ReadyCV.objects.get(user=request.user)
    except:
        pass

    if request.user.id != id:
        return redirect('/')

    if request.method == "POST":
        if 'update_account' in request.POST:
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            user.fullname = fullname
            user.phone_number = phone_number
            user.email = email
            user.address = address
            user.save()

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
                    user = authenticate(username=user.username, password=new_password1)
                    if user:
                        login(request, user)

                    messages.success(request, 'Пароль успешно изменен.')

        if 'profile_images' in request.POST:
            username = request.POST.get('username')
            profile_image = request.FILES.get('profile_image')
            user.username = username
            if profile_image:
                user.profile_image = profile_image
            user.save()

        if 'update_cv' in request.POST:
            avatar = request.FILES.get('avatar')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            citizenship = request.POST.get('citizenship')
            birthday = request.POST.get('birthday')
            gender = request.POST.get('gender')
            child_name = request.POST.get('child_name')
            child_birthday = request.POST.get('child_birthday')
            source = request.POST.get('source')
            reason = request.POST.get('reason')
            interested_position = request.POST.get('interested_position')
            test_year = request.POST.get('test_year')
            test_score = request.POST.get('test_score')
            exam_year = request.POST.get('exam_year')
            exam_score = request.POST.get('exam_score')
            education_info = request.POST.get('education_info')
            qualification_name = request.POST.get('qualification_name')
            qualification_country = request.POST.get('qualification_country')
            qualification_city = request.POST.get('qualification_city')
            qualification_start = request.POST.get('qualification_start')
            qualification_end = request.POST.get('qualification_end')
            organisation_name = request.POST.get('organisation_name')
            organisation_address = request.POST.get('organisation_address')
            job_title = request.POST.get('job_title')
            last_job_start = request.POST.get('last_job_start')
            last_job_end = request.POST.get('last_job_end')
            base_moves = request.POST.get('base_moves')
            dissmissal_reason = request.POST.get('dissmissal_reason')
            advisor = request.POST.get('advisor')
            advisor_organisation = request.POST.get('advisor_organisation')
            advisor_start = request.POST.get('advisor_start')
            advisor_end = request.POST.get('advisor_end')
            advisor_address = request.POST.get('advisor_address')
            advisor_phone = request.POST.get('advisor_phone')
            advisor_socials = request.POST.get('advisor_socials')
            advisor_job = request.POST.get('advisor_job')
            internship_salary = request.POST.get('internship_salary')
            job_salary = request.POST.get('job_salary')
            language = request.POST.get('language')
            language_knowledge = request.POST.get('language_knowledge')
            language_years = request.POST.get('language_years')
            docs = request.POST.get('docs')
            tables = request.POST.get('tables')
            presentation = request.POST.get('presentation')
            prezi = request.POST.get('prezi')
            touch_typing = request.POST.get('touch_typing')
            abroad_country = request.POST.get('abroad_country')
            abroad_start = request.POST.get('abroad_start')
            abroad_end = request.POST.get('abroad_end')
            abroad_reason = request.POST.get('abroad_reason')
            good_skills = request.POST.get('good_skills')
            linkedin = request.POST.get('linkedin')
            facebook = request.POST.get('facebook')
            twitter = request.POST.get('twitter')
            university = request.POST.get('university')
            faculty = request.POST.get('faculty')
            edu_start = request.POST.get('edu_start')
            edu_end = request.POST.get('edu_end')
            edu_country = request.POST.get('edu_country')
            edu_city = request.POST.get('edu_city')
            plan = request.POST.get('plan')
            hobby = request.POST.get('hobby')
            who = request.POST.get('who')
            top_qualities = request.POST.get('top_qualities')
            worst_qualities = request.POST.get('worst_qualities')
            acq = request.POST.get('acq')
            acq_org = request.POST.get('acq_org')
            acq_title = request.POST.get('acq_title')
            acq_start = request.POST.get('acq_start')
            acq_end = request.POST.get('acq_end')
            acq_address = request.POST.get('acq_address')
            acq_phone = request.POST.get('acq_phone')
            acq_email = request.POST.get('acq_email')
            acq_socials = request.POST.get('acq_socials')
            achievement = request.POST.get('achievement')
            knowledge = request.POST.get('knowledge')
            historical_person = request.POST.get('historical_person')
            laptop = request.POST.get('laptop')
            change = request.POST.get('change')
            
            if avatar:
                cv.avatar = avatar

            if advisor_job:
                cv.advisor_job = advisor_job

            if abroad_country:
                cv.abroad_country = abroad_country

            if not test_year:
                test_year = None
            
            if not test_score:
                test_score= None
            
            if not exam_year:
                exam_year= None

            if not exam_score:
                exam_score= None

            if not education_info:
                education_info= None
            
            if not docs:
                docs= False
            
            if not tables:
                tables= False
            
            if not presentation:
                presentation= False

            if not prezi:
                prezi= False

            if not touch_typing:
                touch_typing= False
                

            cv.phone_number = phone_number
            cv.address = address
            cv.citizenship = citizenship
            cv.birthday = birthday
            cv.gender = gender
            cv.child_name = child_name
            cv.child_birthday = child_birthday
            cv.source = source
            cv.reason = reason
            cv.interested_position = interested_position
            cv.test_year = test_year
            cv.test_score = test_score
            cv.exam_year = exam_year
            cv.exam_score = exam_score
            cv.education_info = education_info
            cv.qualification_name = qualification_name
            cv.qualification_country = qualification_country
            cv.qualification_city = qualification_city
            cv.qualification_start = qualification_start
            cv.qualification_end = qualification_end
            cv.organisation_name = organisation_name
            cv.organisation_address = organisation_address
            cv.job_title = job_title
            cv.last_job_start = last_job_start
            cv.last_job_end = last_job_end
            cv.base_moves = base_moves
            cv.dismissal_reason = dissmissal_reason
            cv.advisor = advisor
            cv.advisor_organisation = advisor_organisation
            cv.advisor_start = advisor_start
            cv.advisor_end = advisor_end
            cv.advisor_address = advisor_address
            cv.advisor_phone = advisor_phone
            cv.advisor_socials = advisor_socials
            cv.internship_salary = internship_salary
            cv.job_salary = job_salary
            cv.language = language
            cv.language_knowledge = language_knowledge
            cv.language_years = language_years
            cv.google_docs = docs
            cv.google_tables = tables
            cv.google_presentation = presentation
            cv.prezi = prezi
            cv.touch_typing = touch_typing
            cv.abroad_start = abroad_start
            cv.abroad_end = abroad_end
            cv.abroad_reason = abroad_reason
            cv.good_skills = good_skills
            cv.linkedin = linkedin
            cv.facebook = facebook
            cv.twitter = twitter
            cv.university = university
            cv.faculty = faculty
            cv.edu_start = edu_start
            cv.edu_end = edu_end
            cv.edu_country = edu_country
            cv.edu_city = edu_city
            cv.plan = plan
            cv.hobby = hobby
            cv.who = who
            cv.top_qualities = top_qualities
            cv.worst_qualities = worst_qualities
            cv.acq = acq
            cv.acq_org = acq_org
            cv.acq_title = acq_title
            cv.acq_start = acq_start
            cv.acq_end = acq_end
            cv.acq_address = acq_address
            cv.acq_phone = acq_phone
            cv.acq_email = acq_email
            cv.acq_socials = acq_socials
            cv.achievement = achievement
            cv.knowledge = knowledge
            cv.historical_person = historical_person
            cv.laptop = laptop
            cv.change = change
        
            cv.save()

        if 'update_ready_cv' in request.POST:
            avatar = request.FILES.get('avatar')
            cv_file = request.FILES.get('cv_file')

            if avatar:
                ready_cv.avatar = avatar

            if cv_file:
                if not cv_file.name.endswith(('.pdf', '.docx')):
                    messages.error(request, 'Пожалуйста, загрузите резюме в формате PDF или Word.')
                else:
                    ready_cv.cv_file = cv_file
                    
            ready_cv.save()
            
    return render(request, 'users/settings-profile.html', locals())

def get_latest_settings():
    return Settings.objects.latest('id')

