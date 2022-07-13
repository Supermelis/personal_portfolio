from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.blog, name="all_blogs"),
    path('<int:article_id>/', views.detail, name="detail"),
]