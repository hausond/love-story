from __future__ import annotations

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from memories.models import Event, MainInfo, Photo, Plan, Quote


DATE_INPUT_ATTRS = {
    "class": "w-full rounded-2xl border-0 bg-[#FFF8FA] px-4 py-3 shadow-inner shadow-[rgba(255,182,193,0.25)] focus:ring-2 focus:ring-[#FFB6C1]",
    "type": "date",
}

TEXT_INPUT_ATTRS = {
    "class": "w-full rounded-2xl border-0 bg-[#FFF8FA] px-4 py-3 shadow-inner shadow-[rgba(255,182,193,0.25)] focus:ring-2 focus:ring-[#FFB6C1]",
}

TEXTAREA_ATTRS = {
    **TEXT_INPUT_ATTRS,
    "rows": 4,
}

CHECKBOX_ATTRS = {
    "class": "h-5 w-5 rounded-full border-[#FFB6C1] text-[#FF7F9F] focus:ring-0",
}


class BaseStyledModelForm(forms.ModelForm):
    def _apply_common_styles(self) -> None:
        for field_name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.widgets.DateInput):
                widget.attrs.update(DATE_INPUT_ATTRS)
            elif isinstance(widget, forms.widgets.Textarea):
                widget.attrs.update(TEXTAREA_ATTRS)
            elif isinstance(widget, forms.widgets.CheckboxInput):
                widget.attrs.update(CHECKBOX_ATTRS)
            elif isinstance(widget, forms.widgets.ClearableFileInput):
                widget.attrs.update(
                    {
                        "class": "js-crop-input block w-full rounded-2xl border-0 bg-[#FFF8FA] px-4 py-3 shadow-inner shadow-[rgba(255,182,193,0.25)] focus:ring-2 focus:ring-[#FFB6C1]",
                    }
                )
            else:
                widget.attrs.update(TEXT_INPUT_ATTRS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_common_styles()


class EventForm(BaseStyledModelForm):
    class Meta:
        model = Event
        fields = ("title", "date", "description", "photo")
        widgets = {
            "date": forms.DateInput(),
            "description": forms.Textarea(),
        }


class PhotoForm(BaseStyledModelForm):
    class Meta:
        model = Photo
        fields = ("title", "category", "image")


class QuoteForm(BaseStyledModelForm):
    class Meta:
        model = Quote
        fields = ("text", "author")
        widgets = {
            "text": forms.Textarea({"rows": 3}),
        }


class PlanForm(BaseStyledModelForm):
    class Meta:
        model = Plan
        fields = ("title", "done")


class MainInfoForm(BaseStyledModelForm):
    class Meta:
        model = MainInfo
        fields = ("hero_title", "hero_subtitle", "start_date", "hero_image")
        widgets = {
            "start_date": forms.DateInput(),
            "hero_subtitle": forms.Textarea({"rows": 3}),
        }


class RomanticLoginForm(AuthenticationForm):
    """
    Custom login form that applies romantic pastel styling to auth fields.
    """

    base_attrs = {
        "class": "w-full rounded-2xl border-0 bg-[#FFF8FA] px-4 py-3 shadow-inner shadow-[rgba(255,182,193,0.25)] focus:ring-2 focus:ring-[#FFB6C1]",
        "autocomplete": "off",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        username_widget = self.fields["username"].widget
        password_widget = self.fields["password"].widget
        username_widget.attrs.update(
            {
                **self.base_attrs,
                "placeholder": "Введите логин",
            }
        )
        password_widget.attrs.update(
            {
                **self.base_attrs,
                "placeholder": "Введите пароль",
            }
        )
        self.fields["username"].label = "Логин"
        self.fields["password"].label = "Пароль"
