from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals_index, name='index'),
    path('animals/<int:animal_id>/', views.info, name='info'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animals_create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete'),
    path('animals/<int:animal_id>/add_medication/', views.add_medication, name='add_medication'),
    path('zookeepers/', views.zookeepers_index, name='zookeepers_index'),
    path('zookeepers/<int:zookeeper_id>/', views.zookeeper_info, name='zookeeper_info'),
    path('zookeepers/create/', views.ZookeepersCreate.as_view(), name='zookeepers_create'),
    path('zookeepers/<int:pk>/update/', views.ZookeeperUpdate.as_view(), name='zookeepers_update'),
    path('zookeepers/<int:pk>/delete/', views.ZookeeperDelete.as_view(), name='zookeepers_delete'),
    path('animals/<int:animal_id>/assoc_zookeeper/<int:zookeeper_id>/', views.assoc_zookeeper, name='assoc_zookeeper'),
]