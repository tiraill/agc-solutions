import logging
from typing import List
from django.shortcuts import render
from agc.models import ImageStorage, FeedbackHistory, EmailReceivers
from django.forms import ModelForm, TextInput, BooleanField, CheckboxInput

from django.core.mail import EmailMessage
from agc_django.settings import EMAIL_SENDER


log = logging.getLogger(__name__)
# Create your views here.


class FeedbackForm(ModelForm):
    check = BooleanField(required=True, widget=CheckboxInput(attrs={'checked': 'checked'}))

    class Meta:
        model = FeedbackHistory
        fields = ['first_name', 'email', 'phone_number']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': TextInput(attrs={'placeholder': 'Ваше email'}),
            'phone_number': TextInput(attrs={'placeholder': 'Ваше телефон', 'class': 'phone-mask'}),
        }


def index(request):
    images: List[ImageStorage] = ImageStorage.objects.all()
    ctx = {
        'images': {image.name: image.image.url for image in images},
        'contact_form': FeedbackForm()
    }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            send_new_feedback_email(form)

    return render(
        request,
        template_name="index.html",
        context=ctx
    )


def send_new_feedback_email(form: FeedbackForm):
    body = f'''Поступила новая заявка
            Имя: {form.data['first_name']}
            Email: {form.data['email']}
            Телефон: {form.data['phone_number']}
            '''
    email = EmailMessage(
        from_email=EMAIL_SENDER,
        subject='Новая заявка',
        body=body
    )
    receivers = EmailReceivers.objects.filter(is_send_email_notifications=True)
    if receivers:
        email.to = [user.email for user in receivers]
        try:
            email.send()
        except Exception as exc:
            log.exception(exc)
