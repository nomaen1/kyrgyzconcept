from django.db import models
from django_resized.forms import ResizedImageField 
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

from apps.users.models import User

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
        
class Jobs(models.Model):
    category = models.ForeignKey(Category, related_name="blog_category", on_delete=models.CASCADE, verbose_name="Категории")
    image = ResizedImageField(force_format="WEBP", quality=100, upload_to='jobs_image/', default="/jobs_image/blank_avatar.jpg", verbose_name="Фотография", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии")
    money = models.CharField(max_length=255, verbose_name="Зарплата", blank=True, null=True)
    work = models.CharField(max_length=255, verbose_name="Должность", blank=True, null=True)
    oclock = models.CharField(max_length=255, verbose_name="Часы работы", blank=True, null=True)
    responsiblities = RichTextField(verbose_name="Обязанности")
    expectations = RichTextField(verbose_name="Ожидание")
    experience = models.CharField(max_length=255, verbose_name="Опыт", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

class CV(models.Model):
    user = models.ForeignKey(User, related_name="user_cv", verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="user_cvs/", verbose_name="Аватар")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    citizenship = models.CharField(max_length=100, verbose_name="Гражданство")
    birthday = models.DateField(max_length=100, verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, default=None, verbose_name="Пол")
    children = models.BooleanField(default=False, verbose_name="Есть ли у Вас дети?")
    child_name = models.CharField(max_length=100, verbose_name="Имя ребенка", blank=True, null=True)
    child_birthday = models.DateField(max_length=100, verbose_name="День рождение", blank=True, null=True)
    source = models.CharField(max_length=100, verbose_name="Источник информации о вакансии")
    reason = models.CharField(max_length=250, verbose_name="Почему Вы выбрали именно эту эпозицию?")
    interested = models.BooleanField(default=False, verbose_name="Готовы ли рассматривать другие позиции в Kyrgyz Concept?")
    interested_position = models.CharField(max_length=250, verbose_name="Укажите интересные для вас позиции", blank=True, null=True)
    candidate = models.BooleanField(default=False, verbose_name="Можем ли мы рассматривать Вашу кандидатуру для наших партнеров?")
    republic_test = models.BooleanField(default=False, verbose_name="Проходили ли Вы общереспубликанское тестирование?")
    test_year = models.IntegerField(verbose_name="Год",blank=True, null=True )
    test_score = models.IntegerField(verbose_name="Балл", blank=True, null=True)
    ielts_toefl = models.BooleanField(default=False, verbose_name="Сдавали ли Вы TOEFL/IELTS?")
    exam_year = models.IntegerField(verbose_name="Год", blank=True, null=True)
    exam_score = models.IntegerField(verbose_name="Балл", blank=True, null=True)
    education = models.BooleanField(default=False, verbose_name="Собираетесь ли Вы в течение ближайших трех лет продолжить свое образование?")
    education_info = models.TextField(verbose_name="Дальнейшее обучение", blank=True, null=True)
    qualification = models.BooleanField(default=False, verbose_name="Повышение квалификации (участие в семинарах, тренингах, наличие сертификатов, прохождение курсов)")
    qualification_name = models.CharField(max_length=100, verbose_name="Название квалификации", blank=True, null=True)
    qualification_country = models.CharField(max_length=100, verbose_name="Страна квалификации", blank=True, null=True)
    qualification_city = models.CharField(max_length=100, verbose_name="Город квалификации", blank=True, null=True)
    qualification_start = models.DateField(verbose_name="Дата начала", blank=True, null=True)
    qualification_end= models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    organisation_name = models.CharField(max_length=100, verbose_name="Название организации")
    organisation_address = models.CharField(max_length=100, verbose_name="Адрес организации")
    job_title = models.CharField(max_length=100, verbose_name="Должность")
    last_job_start = models.DateField(verbose_name="Дата начала", blank=True, null=True)
    last_job_end= models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    job_title_duty = models.CharField(max_length=100, verbose_name="Должностные обязанности")
    base_moves = models.CharField(max_length=100, verbose_name="Основные движения")
    dismissal_reason = models.CharField(max_length=100, verbose_name="Причина увольнения", blank=True, null=True)
    advisor= models.CharField(max_length=100, verbose_name="ФИО", null=True)
    advisor_organisation = models.CharField(max_length=100, verbose_name="Название организации")
    advisor_start = models.DateField( verbose_name="Дата начала", blank=True, null=True)
    advisor_end= models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    advisor_address = models.CharField(max_length=100, verbose_name="Адрес")
    advisor_phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    advisor_socials = models.CharField(max_length=250, verbose_name="Соц сети рекомендателя", blank=True, null=True)
    advisor_job = models.CharField(max_length=100, verbose_name="Должность рекомендателя")
    internship_salary = models.IntegerField(verbose_name="Желаемый размер Вашего вознаграждения на стажерский период")
    job_salary = models.IntegerField(verbose_name="Желаемый размер Вашего вознаграждения на основной период")
    language = models.CharField(max_length=100, verbose_name="Знание языков")
    language_knowledge = models.CharField(max_length=100, verbose_name="Степень знания")
    language_years = models.CharField(max_length=100, verbose_name="Сколько лет изучал")
    google_docs = models.BooleanField(default=False, verbose_name="Google Документы", blank=True, null=True)
    google_tables = models.BooleanField(default=False, verbose_name="Google Таблицы", blank=True, null=True)
    google_presentation = models.BooleanField(default=False, verbose_name="Google Презентации", blank=True, null=True)
    prezi = models.BooleanField(default=False, verbose_name="Prezi", blank=True, null=True)
    touch_typing = models.BooleanField(default=False, verbose_name="Слепая печать", blank=True, null=True)
    abroad_country = models.CharField(max_length=100, verbose_name="Пребывание за границей")
    abroad_start = models.DateField(verbose_name="Дата начала", blank=True, null=True)
    abroad_end = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    abroad_reason = models.CharField(max_length=100, verbose_name="Причина визита")
    good_skills = models.CharField(max_length=250, verbose_name="Полезные навыки")
    linkedin = models.URLField(verbose_name="Linkedin")
    facebook = models.URLField(verbose_name="Facebook")
    twitter = models.URLField(verbose_name="Twitter")
    university = models.CharField(max_length=255, verbose_name="Университет", null=True, blank=True)
    faculty = models.CharField(max_length=255, verbose_name="Факультет", null=True, blank=True)
    edu_start = models.DateField(verbose_name="Начало обучения", null=True, blank=True)
    edu_end = models.DateField(verbose_name="Конец обучения", null=True, blank=True)
    edu_country = models.CharField(max_length=255, verbose_name="Страна Университета", null=True, blank=True)
    edu_city = models.CharField(max_length=255, verbose_name="Город Университета", null=True, blank=True)
    plan = models.CharField(max_length=255, verbose_name="Какие у Вас планы на ближайшие 3 - 5 лет?", null=True, blank=True)
    hobby = models.CharField(max_length=255, verbose_name="Ваши увлечения, хобби", null=True, blank=True)
    who = models.CharField(max_length=255, verbose_name="Кто такой Джон Голт?", null=True, blank=True)
    top_qualities = models.CharField(max_length=255, verbose_name="Назовите 3 Ваших лучших качества (которые будут полезны в Вашей работе)", null=True, blank=True)
    worst_qualities = models.CharField(max_length=255, verbose_name="Назовите 3 Ваших худщих качества (которые будут полезны в Вашей работе)", null=True, blank=True)
    acq = models.CharField(max_length=255, verbose_name="ФИО", null=True, blank=True)
    acq_org = models.CharField(max_length=255, verbose_name="Организация", null=True, blank=True)
    acq_title = models.CharField(max_length=255, verbose_name="Должность", null=True, blank=True)
    acq_start = models.DateField(verbose_name="Дата начала", null=True, blank=True)
    acq_end = models.DateField(verbose_name="Дата конца", null=True, blank=True)
    acq_address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    acq_phone = models.CharField(max_length=255, verbose_name="Телефон", null=True, blank=True)
    acq_email = models.CharField(max_length=255, verbose_name="Emaik", unique=True, null=True, blank=True)
    acq_socials = models.CharField(max_length=255, verbose_name="Аккаунт в соц.сетях", null=True, blank=True)
    achievement = models.CharField(max_length=255, verbose_name="Опишите какое-либо свое достижение за последние три года (которое характеризует Вас как личность, подходящую для занятия позиции в Компании)", null=True, blank=True)
    knowledge = models.CharField(max_length=255, verbose_name="Что Вам известно о компании Kyrgyz Concept? Почему Вы хотите с ней сотрудничать?", null=True, blank=True)
    historical_person = models.CharField(max_length=255, verbose_name="Назовите историческую личность, которой Вы восхищаетесь, и объясните Ваш выбор", null=True, blank=True)
    laptop = models.BooleanField(verbose_name="Имеется ли у Вас ноутбук?", default=False, null=True, blank=True)
    change = models.CharField(max_length=255, verbose_name="Что в предложенной форме резюме Вы предложили бы изменить?", null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
    
class ReadyCV(models.Model):
    user = models.ForeignKey(User, related_name="user_ready_cv", verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="user_cvs/", verbose_name="Аватар")
    cv_file = models.FileField(upload_to="CVs/", verbose_name="Резюме")

    def __str__(self) -> str:
        return f"{self.user}"
    
    class Meta:
        verbose_name = "Готовое Резюме"
        verbose_name_plural = "Готовые Резюме"
    