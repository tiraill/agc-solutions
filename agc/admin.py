from django.contrib import admin

from .models import ImageStorage, FeedbackHistory, EmailReceivers, OrderHistory


@admin.register(ImageStorage)
class ImageStorageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone_number', 'creation_date')
    search = ('email', 'phone_number')
    list_filter = ('creation_date',)
    ordering = ('creation_date',)


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'creation_date')
    search = ('email', 'phone_number')
    list_filter = ('creation_date',)
    ordering = ('creation_date',)


@admin.register(EmailReceivers)
class EmailReceiversAdmin(admin.ModelAdmin):
    list_display = ('email',)
