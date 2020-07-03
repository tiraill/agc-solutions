from django.urls import path

from .views import index, order

urlpatterns = [
    path('', index, name="agc-index"),
    path('order/', order, name="agc-order"),
]
