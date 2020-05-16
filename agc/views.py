import logging
from typing import Union
from django.shortcuts import render
from django.http import Http404
from agc.models import EmailReceivers

from django.core.mail import EmailMessage
from agc_django.settings import EMAIL_SENDER
from agc.forms import FeedbackForm, OrderForm

log = logging.getLogger(__name__)


def index(request):
    ctx = {
        'contact_form': FeedbackForm(),
        'order_form': OrderForm()
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


def order(request):
    if request.method == 'POST':
        ctx = {
            'contact_form': FeedbackForm()
        }
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            send_new_feedback_email(form)
            return render(request, 'index.html', context=ctx)
        ctx.update({'order_form': OrderForm(form)})
        return render(request, 'index.html', context=ctx)
    raise Http404()


def send_new_feedback_email(form: Union[FeedbackForm, OrderForm]):
    receivers = EmailReceivers.objects.filter(is_send_email_notifications=True)
    if receivers:
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
        email.to = [user.email for user in receivers]
        try:
            email.send()
        except Exception as exc:
            log.exception(exc)
