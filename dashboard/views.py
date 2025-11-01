from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from memories.models import Event, MainInfo, Photo, Plan, Quote

from .forms import EventForm, MainInfoForm, PhotoForm, PlanForm, QuoteForm

ROMANTIC_SUCCESS = "Сохранено с любовью 💕"


def redirect_to_home(request: HttpRequest) -> HttpResponse:
    return redirect("dashboard:home")


@login_required
def home(request: HttpRequest) -> HttpResponse:
    context = {
        "events_count": Event.objects.count(),
        "photos_count": Photo.objects.count(),
        "quotes_count": Quote.objects.count(),
        "plans_count": Plan.objects.count(),
        "plans_done": Plan.objects.filter(done=True).count(),
        "main_info": MainInfo.objects.first(),
    }
    return render(request, "dashboard/home.html", context)


@login_required
def event_list(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    events = Event.objects.all()
    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    events = events.order_by("-date")
    return render(
        request,
        "dashboard/events/list.html",
        {"events": events, "query": query},
    )


@login_required
def event_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:events")
    else:
        form = EventForm()
    return render(request, "dashboard/events/form.html", {"form": form, "title": "Новое событие"})


@login_required
def event_edit(request: HttpRequest, pk: int) -> HttpResponse:
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:events")
    else:
        form = EventForm(instance=event)
    return render(request, "dashboard/events/form.html", {"form": form, "title": "Редактировать событие", "object": event})


@login_required
def event_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method != "POST":
        return HttpResponseForbidden()
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "Удалено с любовью 💔")
    return redirect("dashboard:events")


@login_required
def photo_list(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", "").strip()
    photos = Photo.objects.all()
    if query:
        photos = photos.filter(Q(title__icontains=query) | Q(category__icontains=query))
    photos = photos.order_by("title")
    return render(
        request,
        "dashboard/photos/list.html",
        {"photos": photos, "query": query},
    )


@login_required
def photo_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:photos")
    else:
        form = PhotoForm()
    return render(request, "dashboard/photos/form.html", {"form": form, "title": "Добавить фото"})


@login_required
def photo_edit(request: HttpRequest, pk: int) -> HttpResponse:
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:photos")
    else:
        form = PhotoForm(instance=photo)
    return render(request, "dashboard/photos/form.html", {"form": form, "title": "Редактировать фото", "object": photo})


@login_required
def photo_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method != "POST":
        return HttpResponseForbidden()
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    messages.success(request, "Удалено с любовью 💔")
    return redirect("dashboard:photos")


@login_required
def quote_list(request: HttpRequest) -> HttpResponse:
    quotes = Quote.objects.order_by("author")
    return render(request, "dashboard/quotes/list.html", {"quotes": quotes})


@login_required
def quote_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:quotes")
    else:
        form = QuoteForm()
    return render(request, "dashboard/quotes/form.html", {"form": form, "title": "Добавить цитату"})


@login_required
def quote_edit(request: HttpRequest, pk: int) -> HttpResponse:
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:quotes")
    else:
        form = QuoteForm(instance=quote)
    return render(request, "dashboard/quotes/form.html", {"form": form, "title": "Редактировать цитату", "object": quote})


@login_required
def quote_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method != "POST":
        return HttpResponseForbidden()
    quote = get_object_or_404(Quote, pk=pk)
    quote.delete()
    messages.success(request, "Удалено с любовью 💔")
    return redirect("dashboard:quotes")


@login_required
def plan_list(request: HttpRequest) -> HttpResponse:
    plans = Plan.objects.order_by("done", "title")
    return render(request, "dashboard/plans/list.html", {"plans": plans})


@login_required
def plan_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:plans")
    else:
        form = PlanForm()
    return render(request, "dashboard/plans/form.html", {"form": form, "title": "Добавить план"})


@login_required
def plan_edit(request: HttpRequest, pk: int) -> HttpResponse:
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:plans")
    else:
        form = PlanForm(instance=plan)
    return render(request, "dashboard/plans/form.html", {"form": form, "title": "Редактировать план", "object": plan})


@login_required
def plan_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method != "POST":
        return HttpResponseForbidden()
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    messages.success(request, "Удалено с любовью 💔")
    return redirect("dashboard:plans")


@login_required
def settings_view(request: HttpRequest) -> HttpResponse:
    instance = MainInfo.objects.first()
    if request.method == "POST":
        form = MainInfoForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save()
            messages.success(request, ROMANTIC_SUCCESS)
            return redirect("dashboard:settings")
    else:
        form = MainInfoForm(instance=instance)
    return render(
        request,
        "dashboard/settings.html",
        {"form": form, "instance": instance},
    )
