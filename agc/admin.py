from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import ImageStorage, FeedbackHistory,\
    EmailReceivers, OrderHistory, GlassElement, GlassElementImage


# @admin.register(ImageStorage)
# class ImageStorageAdmin(admin.ModelAdmin):
#     list_display = ('name',)


@admin.register(GlassElement)
class GlassElementAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'cols': 80, 'rows': 5})},
    }

    list_display = ('title',)
    search_fields = ('title',)


@admin.register(GlassElementImage)
class GlassElementImageAdmin(admin.ModelAdmin):
    list_display = ('uid', 'get_glass_element', 'priority')
    list_filter = ('element__title',)
    search_fields = ('element__title',)
    autocomplete_fields = ('element',)
    exclude = ('uid', 'sm_image')

    def get_glass_element(self, instance):
        if instance and instance.element:
            return instance.element.title
        else:
            return f"Производитель не указан, либо был удален"
    get_glass_element.short_description = "Наименование производителя стекла, к которому прикреплено фото"


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number', 'creation_date')
    search_fields = ('email', 'phone_number')
    list_filter = ('creation_date',)
    ordering = ('creation_date',)


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'creation_date')
    search_fields = ('email', 'phone_number')
    list_filter = ('creation_date',)
    ordering = ('creation_date',)


@admin.register(EmailReceivers)
class EmailReceiversAdmin(admin.ModelAdmin):
    list_display = ('email',)
