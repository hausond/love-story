from __future__ import annotations

from django.db import models


class MainInfo(models.Model):
    start_date = models.DateField("Дата знакомства")
    hero_title = models.CharField("Заголовок героя", max_length=150)
    hero_subtitle = models.CharField("Подзаголовок героя", max_length=255)
    hero_image = models.ImageField("Главное фото", upload_to="hero/", blank=True, null=True)

    class Meta:
        verbose_name = "Основная информация"
        verbose_name_plural = "Основная информация"

    def __str__(self) -> str:
        return "Главная информация"


class Event(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    date = models.DateField("Дата")
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to="events/", blank=True, null=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self) -> str:
        return f"{self.title} — {self.date:%d.%m.%Y}"


class Photo(models.Model):
    title = models.CharField("Название", max_length=150)
    image = models.ImageField("Фото", upload_to="gallery/")
    category = models.CharField("Категория", max_length=100, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

    def __str__(self) -> str:
        return self.title


class Quote(models.Model):
    text = models.TextField("Текст")
    author = models.CharField("Автор", max_length=100)

    class Meta:
        ordering = ["author"]
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

    def __str__(self) -> str:
        return f"{self.author}: {self.text[:40]}..."


class Plan(models.Model):
    title = models.CharField("План / мечта", max_length=200)
    done = models.BooleanField("Выполнено", default=False)

    class Meta:
        ordering = ["done", "title"]
        verbose_name = "План"
        verbose_name_plural = "Планы"

    def __str__(self) -> str:
        return self.title
