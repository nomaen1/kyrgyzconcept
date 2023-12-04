from django.urls import path
from apps.jobs import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('jobs/<int:id>/', views.jobs_detail,name = "job_detail"),
    path('cv', views.cv, name = "cv"),
    path('cv_add', views.cv_add, name = "cv_add"),
    path('cv_download', views.cv_download,name = "cv_download"),
]