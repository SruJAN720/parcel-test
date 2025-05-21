from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }
