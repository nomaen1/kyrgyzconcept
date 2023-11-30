from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from apps.users.models import Settings
from apps.jobs.models import Jobs, CV, ReadyCV

#JOB

def jobs_all(request):
    jobs = Jobs.objects.all()
    setting = Settings.objects.latest('id')
    return render(request, "jobs/company_listing.html", locals())

@login_required(login_url='login')
def jobs_detail(request, id):
    setting = Settings.objects.latest('id')
    job = Jobs.objects.get(id=id)
    jobs_category = Jobs.objects.filter(category=job.category).order_by('category')

    return render(request, 'jobs/listing_single.html', locals())


# CV
def cv(request):
    setting = Settings.objects.latest('id')

    return render(request, "jobs/cv.html", locals())

def cv_add(request):
    setting = Settings.objects.latest('id')

    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        citizenship = request.POST.get('citizenship')
        birthday_str = request.POST.get('birthday')
        gender = request.POST.get('gender')
        children = request.POST.get('child_yes') == True
        child_no = request.POST.get('child_no')
        child_name = request.POST.get('child_name')
        child_birthday_str = request.POST.get('child_birthday')
        source = request.POST.get('source')
        reason = request.POST.get('reason')
        interested_position = request.POST.get('interested_yes') == True
        interested_no = request.POST.get('interested_no')
        candidate = request.POST.get('candidate_yes') == True
        candidate_no = request.POST.get('candidate_no')
        test = request.POST.get('test_yes') == "True"
        test_no = request.POST.get('test_no')
        test_year= request.POST.get('test_year')
        test_score = request.POST.get('test_score')
        exam = request.POST.get('exam_yes') == "True"
        exam_no = request.POST.get('exam_no')
        exam_year = request.POST.get('exam_year')
        exam_score = request.POST.get('exam_score')
        education = request.POST.get('education_yes') == "True"
        education_no = request.POST.get('education_no')
        education_info = request.POST.get('education_info')
        qualification = request.POST.get('qualification_yes') == "True"
        qualification_no = request.POST.get('qualification_no')
        qualification_name = request.POST.get('qualification_name')
        qualification_country = request.POST.get('qualification_country')
        qualification_city = request.POST.get('qualification_city')
        qualification_start = request.POST.get('qualification_start')
        qualification_end = request.POST.get('qualification_end')
        organisation_name = request.POST.get('organisation_name')
        organisation_address = request.POST.get('organisation_address')
        job_title = request.POST.get('job_title')
        last_job_start_str = request.POST.get('last_job_start')
        last_job_end_str = request.POST.get('last_job_end')
        job_title_duty = request.POST.get('job_title_duty')
        base_moves = request.POST.get('base_moves')
        dismissal_reason = request.POST.get('dismissal_reason')
        advisor = request.POST.get('advisor')
        advisor_organisation = request.POST.get('advisor_organisation')
        advisor_start_str = request.POST.get('advisor_start')
        advisor_end_str = request.POST.get('advisor_end')
        advisor_address = request.POST.get('advisor_address')
        advisor_phone = request.POST.get('advisor_phone')
        advisor_socials = request.POST.get('advisor_socials')
        advisor_job = request.POST.get('advisor_job')
        internship_salary = request.POST.get('internship_salary')
        job_salary = request.POST.get('job_salary')
        language = request.POST.get('language')
        language_knowledge = request.POST.get('language_knowledge')
        language_years = request.POST.get('language_years')
        docs = request.POST.get('docs') == True
        tables = request.POST.get('tables') == True
        presentaions = request.POST.get('presentaions') == True
        prezi = request.POST.get('prezi') == "True"
        touch_typing = request.POST.get('touch_typing') == True
        abroad_country = request.POST.get('abroad_country')
        abroad_start_str = request.POST.get('abroad_start')
        abroad_end_str = request.POST.get('abroad_end')
        abroad_reason = request.POST.get('abroad_reason')
        good_skills = request.POST.get('good_skills')
        linkedin = request.POST.get('linkedin')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')

        print(children)


        if birthday_str and child_birthday_str and last_job_start_str and last_job_end_str and advisor_start_str and advisor_end_str and abroad_start_str and abroad_end_str:
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
            child_birthday = datetime.strptime(child_birthday_str, '%Y-%m-%d').date()
            last_job_start = datetime.strptime(last_job_start_str, '%Y-%m-%d').date()
            last_job_end = datetime.strptime(last_job_end_str, '%Y-%m-%d').date()
            advisor_start = datetime.strptime(advisor_start_str, '%Y-%m-%d').date()
            advisor_end = datetime.strptime(advisor_end_str, '%Y-%m-%d').date()
            abroad_start = datetime.strptime(abroad_start_str, '%Y-%m-%d').date()
            abroad_end = datetime.strptime(abroad_end_str, '%Y-%m-%d').date()


        cv = CV.objects.create(
            user = request.user,
            avatar = avatar,
            phone_number = phone_number,
            address = address,
            citizenship = citizenship,
            birthday = birthday,
            gender = gender,
            children = children,
            child_name = child_name,
            child_birthday = child_birthday,
            source = source,
            reason = reason,
            interested_position = interested_position,
            candidate = candidate,
            republic_test = test,
            test_year = test_year,
            test_score = test_score,
            ielts_toefl = exam,
            exam_year = exam_year,
            exam_score = exam_score,
            education = education,
            education_info = education_info,
            qualification = qualification,
            qualification_name = qualification_name,
            qualification_country = qualification_country,
            qualification_city = qualification_city,
            qualification_start = qualification_start,
            qualification_end = qualification_end,
            organisation_name = organisation_name,
            organisation_address = organisation_address,
            job_title = job_title,
            last_job_start = last_job_start,
            last_job_end = last_job_end,
            job_title_duty = job_title_duty,
            base_moves = base_moves,
            dismissal_reason = dismissal_reason,
            advisor = advisor,
            advisor_organisation = advisor_organisation,
            advisor_start = advisor_start,
            advisor_end = advisor_end,
            advisor_address = advisor_address,
            advisor_phone = advisor_phone,
            advisor_socials = advisor_socials,
            advisor_job = advisor_job,
            internship_salary = internship_salary,
            job_salary = job_salary,
            language = language,
            language_knowledge = language_knowledge,
            language_years = language_years,
            google_docs = docs,
            google_tables = tables,
            google_presentation = presentaions,
            prezi = prezi,
            touch_typing = touch_typing,
            abroad_country = abroad_country,
            abroad_start = abroad_start,
            abroad_end = abroad_end,
            abroad_reason = abroad_reason,
            good_skills = good_skills,
            linkedin = linkedin,
            facebook = facebook,
            twitter = twitter
        )
        cv.save()

        return redirect("/")

    return render(request, "jobs/add_cv.html", locals())

def cv_download(request):
    setting = Settings.objects.latest('id')

    if request.method == "POST":
        avatar = request.FILES.get('avatar')
        cv_file  = request.FILES.get('cv_file')
        checkbox = request.POST.get('shipping-option')

        if avatar and cv_file:
            existing_cv = ReadyCV.objects.filter(user=request.user).first()
            if checkbox:
                if existing_cv:
                    existing_cv.avatar = avatar
                    existing_cv.cv_file = cv_file
                    existing_cv.save()
                    return redirect("/")
                else:
                    cv = ReadyCV.objects.create(user=request.user, avatar=avatar, cv_file=cv_file)
                    cv.save()
                    return redirect('/')
            else:
                messages.error(request, "Пожалуйста, согласитесь с условиями перед отправкой резюме.")
        else:
            messages.error(request, "Пожалуйста, заполните всю форму.")

    return render(request, "jobs/cv_download.html", locals())