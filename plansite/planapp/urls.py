from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('index1', views.index1, name="index1"),
    path('plan', views.plan, name="plan"),
    path('planlist/', views.planList.as_view()),

]
