from django.urls import path

from . import views

app_name = "memories"

urlpatterns = [
    path("", views.index, name="index"),
    path("timeline/", views.timeline, name="timeline"),
    path("gallery/", views.gallery, name="gallery"),
    path("quotes/", views.quotes, name="quotes"),
    path("plans/", views.plans, name="plans"),
    path("api/plan/<int:pk>/toggle/", views.toggle_plan, name="plan-toggle"),
]
