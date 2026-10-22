from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("<int:tutor_id>/", views.tutor_detail, name="tutor_detail_page")
]
