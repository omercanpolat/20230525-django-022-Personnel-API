from django.urls import path
from .views import (DepartmentListCreateView,
                    DepartmentRUDView,
                    PersonnelListCreateView,
                    PersonnelRUDView,
                    DepartmentPersonnelView)


urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', DepartmentRUDView.as_view()),
    path('personnels/', PersonnelListCreateView.as_view()),
    path('personnels/<int:pk>/', PersonnelRUDView.as_view()),
    # path('department-personnels/', DepartmentPersonnelView.as_view()),
    path('departments/<str:department>/', DepartmentPersonnelView.as_view()),
]
