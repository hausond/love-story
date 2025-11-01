from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Event, MainInfo, Photo, Plan, Quote


class ImagePreviewMixin:
    preview_field = ""

    @admin.display(description="Предпросмотр")
    def image_preview(self, obj):
        field_name = self.preview_field
        if not field_name:
            return "—"
        image = getattr(obj, field_name)
        if image and getattr(image, "url", None):
            return format_html('<img src="{}" style="max-height: 200px;" />', image.url)
        return mark_safe("—")


@admin.register(MainInfo)
class MainInfoAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ("hero_title", "start_date")
    fields = ("start_date", "hero_title", "hero_subtitle", "hero_image", "image_preview")
    readonly_fields = ("image_preview",)
    preview_field = "hero_image"

    def has_add_permission(self, request):
        # Allow only a single MainInfo record.
        if MainInfo.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Event)
class EventAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("date",)
    search_fields = ("title", "description")
    fields = ("title", "date", "description", "photo", "image_preview")
    readonly_fields = ("image_preview",)
    preview_field = "photo"


@admin.register(Photo)
class PhotoAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)
    search_fields = ("title",)
    fields = ("title", "category", "image", "image_preview")
    readonly_fields = ("image_preview",)
    preview_field = "image"


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "short_text")
    search_fields = ("author", "text")

    @admin.display(description="Текст")
    def short_text(self, obj):
        return (obj.text[:50] + "…") if len(obj.text) > 50 else obj.text


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("title", "done")
    list_filter = ("done",)
    search_fields = ("title",)
    list_editable = ("done",)
