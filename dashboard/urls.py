from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import RomanticLoginForm

app_name = "dashboard"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="dashboard/login.html",
            authentication_form=RomanticLoginForm,
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.redirect_to_home, name="root"),
    path("home/", views.home, name="home"),
    path("events/", views.event_list, name="events"),
    path("events/create/", views.event_create, name="event-create"),
    path("events/<int:pk>/edit/", views.event_edit, name="event-edit"),
    path("events/<int:pk>/delete/", views.event_delete, name="event-delete"),
    path("gallery/", views.photo_list, name="photos"),
    path("gallery/create/", views.photo_create, name="photo-create"),
    path("gallery/<int:pk>/edit/", views.photo_edit, name="photo-edit"),
    path("gallery/<int:pk>/delete/", views.photo_delete, name="photo-delete"),
    path("quotes/", views.quote_list, name="quotes"),
    path("quotes/create/", views.quote_create, name="quote-create"),
    path("quotes/<int:pk>/edit/", views.quote_edit, name="quote-edit"),
    path("quotes/<int:pk>/delete/", views.quote_delete, name="quote-delete"),
    path("plans/", views.plan_list, name="plans"),
    path("plans/create/", views.plan_create, name="plan-create"),
    path("plans/<int:pk>/edit/", views.plan_edit, name="plan-edit"),
    path("plans/<int:pk>/delete/", views.plan_delete, name="plan-delete"),
    path("settings/", views.settings_view, name="settings"),
]
