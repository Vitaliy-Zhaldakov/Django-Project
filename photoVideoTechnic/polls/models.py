from django.contrib import admin
from django.db import models


# Create your models here.
class MaxResolution(models.Model):
    resolution = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Максимальное разрешение"
        verbose_name_plural = "Максимальные разрешения"

    def __str__(self):
        return self.resolution


class Type(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Тип фотоаппарата"
        verbose_name_plural = "Типы фотоаппаратов"

    def __str__(self):
        return self.name


class Cameras(models.Model):
    manufacturer = models.CharField(max_length=30, verbose_name="Производитель")
    model = models.CharField(max_length=100, verbose_name="Модель")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип фотоаппарата")
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Фотоаппарат"
        verbose_name_plural = "Фотоаппараты"

    @admin.display(description='Цена')
    def formatPrice(self):
        return str(self.price) + " ₽"

    def __str__(self):
        return str(self.manufacturer + " " + self.model + " " + self.type.name + " " + str(self.price) + "₽")


class VideoCameras(models.Model):
    manufacturer = models.CharField(max_length=30, verbose_name="Производитель")
    model = models.CharField(max_length=100, verbose_name="Модель")
    maxResolution = models.ForeignKey(MaxResolution, on_delete=models.CASCADE, verbose_name="Максимальное разрешение")
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Видеокамера"
        verbose_name_plural = "Видеокамеры"

    @admin.display(description='Цена')
    def formatPrice(self):
        return str(self.price) + " ₽"

    def __str__(self):
        return str(self.manufacturer + " " + self.model + " " + self.maxResolution.resolution + " " + str(self.price)
                   + "₽")


class ActionCameras(models.Model):
    manufacturer = models.CharField(max_length=30, verbose_name="Производитель")
    model = models.CharField(max_length=100, verbose_name="Модель")
    maxResolution = models.ForeignKey(MaxResolution, on_delete=models.CASCADE, verbose_name="Максимальное разрешение")
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Экшн-камера"
        verbose_name_plural = "Экшн-камеры"

    @admin.display(description='Цена')
    def formatPrice(self):
        return str(self.price) + " ₽"

    def __str__(self):
        return str(self.manufacturer + " " + self.model + " " + self.maxResolution.resolution + " " + str(self.price)
                   + "₽")


class Selections(admin.SimpleListFilter):
    title = "Выборка"

    parameter_name = "selection"

    def lookups(self, request, model_admin):
        return (
            ('Slr camera', 'Slr camera'),
            ('Compact camera', 'Compact camera'),
            ('Instant printing camera', 'Instant printing camera'),
            ('Film camera', 'Film camera'),
            ('Camera with interchangeable optics', 'Camera with interchangeable optics')
        )

    def queryset(self, request, queryset):
        if self.value() == 'Slr camera':
            return queryset.filter(Cameras__type='Slr camera')
        if self.value() == 'Compact camera':
            return queryset.filter(Cameras__type='Compact camera')
        if self.value() == 'Instant printing camera':
            return queryset.filter(Cameras__type='Instant printing camera')
        if self.value() == 'Film camera':
            return queryset.filter(Cameras__type='Film camera')
        if self.value() == 'Camera with interchangeable optics':
            return queryset.filter(Cameras__type='Camera with interchangeable optics')

