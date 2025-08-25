from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list_create, name='student_list_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),  # <-- যোগ করো
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),  # <-- optional
]
