import logging
from typing import Union
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import Http404
from agc.models import EmailReceivers, GlassElement, GlassElementImage

from django.core.mail import EmailMessage
from agc_django.settings import EMAIL_SENDER
from agc.forms import FeedbackForm, OrderForm

log = logging.getLogger(__name__)


def get_context():
    glass_elements = GlassElement.objects.all()
    possible_colors = GlassElementImage.objects.all()
    return {
        'glass_elements': glass_elements,
        'possible_colors': possible_colors,
        'contact_form': FeedbackForm(),
        'order_form': OrderForm()
    }


def index(request):
    ctx = get_context()
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
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            send_new_feedback_email(form, order_req=True)
            return HttpResponseRedirect(reverse('agc-index'))
        ctx = get_context()
        ctx.update({
            'order_form': form,
            'error': 'true'
        })
        return render(request, 'index.html', context=ctx)
    raise Http404()


def send_new_feedback_email(form: Union[FeedbackForm, OrderForm], order_req=False):
    receivers = EmailReceivers.objects.filter(is_send_email_notifications=True)
    if receivers:
        subj = 'Новая заявка'
        body = f'''Поступила новая заявка\n
                Имя: {form.data['first_name']}\n
                Email: {form.data['email']}\n
                Телефон: {form.data['phone_number']}\n
                '''
        if order_req:
            subj = 'Новый заказ'
            body += f'''Детали заказа: \n
                        Наименования зон: {form.data['zone_name']}\n
                        Наименования элементов: {form.data['items']}\n
                        Наименования цветов стёкол: {form.data['glass_color']}\n
                        Наименования производителей стёкол: {form.data['glass_name']}\n
                    '''
        email = EmailMessage(
            from_email=EMAIL_SENDER,
            subject=subj,
            body=body
        )
        email.to = [user.email for user in receivers]
        try:
            email.send()
        except Exception as exc:
            log.exception(exc)
