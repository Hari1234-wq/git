
from django.urls import path
from employee.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('<int:id>/details/', employee_details, name="employee_details"),
    path('<int:id>/edit/', employee_edit, name="employee_edit"),
    path('add/', employee_add, name="employee_add"),
    path('<int:id>/delete', employee_delete, name="employee_delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
