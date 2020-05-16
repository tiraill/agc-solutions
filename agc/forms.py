from agc.models import FeedbackHistory, OrderHistory
from django.forms import ModelForm, TextInput, BooleanField, CheckboxInput, HiddenInput


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


class OrderForm(ModelForm):
    check = BooleanField(required=True, widget=CheckboxInput(attrs={'checked': 'checked'}))

    class Meta:
        model = OrderHistory
        fields = ['first_name', 'email', 'phone_number',
                  'zone_name', 'items', 'glass_color',
                  'glass_name']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': TextInput(attrs={'placeholder': 'Ваше email'}),
            'phone_number': TextInput(attrs={'placeholder': 'Ваше телефон', 'class': 'phone-mask'}),
            'zone_name': HiddenInput(),
            'items': HiddenInput(),
            'glass_color': HiddenInput(),
            'glass_name': HiddenInput()
        }
