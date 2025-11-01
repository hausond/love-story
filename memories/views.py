from __future__ import annotations

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Event, MainInfo, Photo, Plan, Quote


def index(request: HttpRequest) -> HttpResponse:
    main_info = MainInfo.objects.first()
    days_together = None
    start_date = None

    if main_info and main_info.start_date:
        start_date = main_info.start_date
        today = timezone.localdate()
        days_together = (today - main_info.start_date).days

    context = {
        "main_info": main_info,
        "main": main_info,
        "days_together": days_together,
        "start_date": start_date,
        "events": Event.objects.all()[:3],
        "photos": Photo.objects.all()[:6],
    }
    return render(request, "memories/index.html", context)


def timeline(request: HttpRequest) -> HttpResponse:
    events = Event.objects.select_related().all()
    return render(request, "memories/timeline.html", {"events": events})


def gallery(request: HttpRequest) -> HttpResponse:
    photos = Photo.objects.all()
    categories = sorted({photo.category for photo in photos if photo.category})
    return render(
        request,
        "memories/gallery.html",
        {"photos": photos, "categories": categories},
    )


def quotes(request: HttpRequest) -> HttpResponse:
    items = Quote.objects.all()
    return render(request, "memories/quotes.html", {"quotes": items})


def plans(request: HttpRequest) -> HttpResponse:
    items = Plan.objects.all()
    return render(request, "memories/plans.html", {"plans": items})


@csrf_exempt
@require_http_methods(["PUT"])
def toggle_plan(request: HttpRequest, pk: int) -> JsonResponse:
    plan = get_object_or_404(Plan, pk=pk)
    plan.done = not plan.done
    plan.save(update_fields=["done"])
    return JsonResponse({"id": plan.pk, "done": plan.done})
