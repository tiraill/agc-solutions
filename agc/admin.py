from django.contrib import admin

from .models import ImageStorage, FeedbackHistory, EmailReceivers


@admin.register(ImageStorage)
class ImageStorageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number', 'data_time')


@admin.register(EmailReceivers)
class EmailReceiversAdmin(admin.ModelAdmin):
    list_display = ('email',)
