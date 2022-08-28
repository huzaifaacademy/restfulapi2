from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeesListApiView.as_view()),
    path('<int:id>/', views.EmployeeDetailAPIView.as_view())
]